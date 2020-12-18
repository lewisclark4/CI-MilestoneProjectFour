const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const errorDiv = document.getElementById('card-errors');
const form = document.getElementById("payment-form")
const checkoutButton = document.getElementById("checkout-button")
const saveInfoCheckBox = document.getElementById("id-save-info")
const csrfTokenInputName = document.getElementsByName("csrfmiddlewaretoken")
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#6c757d',
        fontFamily: '"Quicksand", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', {style: style});


card.mount('#card-element');

card.addEventListener('change', e => {
    if (e.error) {
        errorDiv.innerHTML = `
            <span role="alert">
                <i class="fas fa-exclamation-circle"></i>
            </span>
            <span>${e.error.message}</span>
        `
    } else {
        errorDiv.textContent = ''
    }
})

form.addEventListener('submit', e => {
    e.preventDefault()
    card.update({
        'disabled': true
    })
    checkoutButton.disabled = true
    let saveInfo = Boolean(saveInfoCheckBox.checked)
    let csrfToken = csrfTokenInputName[0].value
    let postData = new FormData()
    postData.append("csrfmiddlewaretoken", csrfToken)
    postData.append("client_secret", clientSecret)
    postData.append("save_info", saveInfo)
    let url = '/checkout/cache_checkout_data/';

    fetch(url, {
        method: 'POST',
        body: postData,
        headers: {
            'X-CSRFToken': csrfToken
        }
    }).then(response => {
        if (!response.ok) {
            location.reload()
        }
    }).then(() => {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                        name: form.full_name.value.trim(),
                        email: form.email.value.trim(),
                        phone: form.phone_number.value.trim(),
                        address: {
                            line1: form.address_1.value.trim(),
                            line2: form.address_2.value.trim(),
                            city: form.city.value.trim(),
                            state: form.county.value.trim(),
                            country: form.country.value.trim(),
                        }
                    },
                },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.address_1.value.trim(),
                    line2: form.address_2.value.trim(),
                    city: form.city.value.trim(),
                    state: form.county.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                }
            }
        }).then(result => {
            if (result.error) {
                errorDiv.innerHTML = `
                    <span role="alert">
                        <i class="fas fa-exclamation-circle"></i>
                    </span>
                    <span>${result.error.message}</span>
                    `
                card.update({
                    'disabled': false
                })
                checkoutButton.disabled = false
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit()
                }
            }
        })
    })
})
