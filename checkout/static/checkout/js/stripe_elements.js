const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
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
let errorDiv = document.getElementById('card-errors');
let form = document.getElementById("payment-form")
let checkoutButton = document.getElementById("checkout-button")

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

form.addEventListener("submit", e => {
    e.preventDefault()
    card.update({
        "disabled": true
    })
    checkoutButton.setAttribute("disabled", "")
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
                "disabled": false
            })
            paymentButton.removeAttribute("disabled")
        } else {
            if (result.paymentIntent.status === "succeeded") {
                form.submit()
            }
        }
    });
});
