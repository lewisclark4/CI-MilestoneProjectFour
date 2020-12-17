const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const errorDiv = document.getElementById('card-errors');
const form = document.getElementById("payment-form")
const checkoutButton = document.getElementById("checkout-button")
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000',
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
        errorDiv.textContent = ""
    }
})

form.addEventListener('submit', e => {
    e.preventDefault()
    card.update({
        'disabled': true
    })
    checkoutButton.disabled = true
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
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
    });
});
