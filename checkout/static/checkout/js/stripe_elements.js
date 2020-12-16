const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
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



var errorDiv = document.getElementById('card-errors');

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