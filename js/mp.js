const mp = new MercadoPago ("TEST-69101bcf-662c-4852-b4e5-eb391316272a", {
    locale: 'es-AR'
});

const buttons = document.getElementsByClassName("welcome_button");

for (let button of buttons) {
    button.addEventListener("click", async () => {
        try {
            const priceInput = document.getElementById("input_price").value;
            // Si el valor del input está presente lo usa, sino usa 1000
            const price = priceInput ? Number(priceInput) : 1000;

            const orderData = {
                title: "Donación",
                quantity: 1,
                price: price, 
            };
            console.log(orderData);
            const response = await fetch("http://localhost:3000/create_preference", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(orderData),
            });
            const preference = await response.json();
            createCheckoutButton(preference.id);
        } catch {
            alert("Error al crear la preferencia aca");
        }
    });
}

const createCheckoutButton = (preferenceId) => {
  const renderComponent = async () => {
    await mp.bricks().create("wallet", "wallet_container", {
      initialization: {
          preferenceId: preferenceId,
          redirectMode: "blank"
      },
   });
  }
  renderComponent();
}
