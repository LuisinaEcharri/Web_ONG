const mp = new MercadoPago ("TEST-aaba47ba-0341-4d4d-a3c0-4f66fef53bbb", {
    locale: 'es-AR'
});

const buttons = document.getElementsByClassName("welcome_button");

for (let button of buttons) {
    button.addEventListener("click", async () => {
        try {
            const orderData = {
                title: "Donación", // esto decis?
                quantity: 1,
                price: 200, // Captura el monto desde el HTML si es necesario
            };
            console.log(orderData);
            //aca esta el error cuando hace el post a la api creo yo
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
            alert("Error al crear la preferencia aca sucio");
        }
    });
}

const createCheckoutButton = (preferenceId) => {
  const renderComponent = async () => {
    await mp.bricks().create("wallet", "wallet_container", {
      initialization: {
          preferenceId: "<PREFERENCE_ID>",
          redirectMode: "blank"
      },
   });
  }
  renderComponent();
}
