let timeoutId;
  // Rest of the click handling logic
  const mp = new MercadoPago("TEST-69101bcf-662c-4852-b4e5-eb391316272a", {
    locale: "es-AR",
  });
  
const handleClick = async (event) => {

  if (timeoutId) {
    clearTimeout(timeoutId);
    return; 
  }

  timeoutId = setTimeout(() => {
    timeoutId = null;
  }, 250);

  let price;
  
  let inputValue = document.getElementById("amount").value;

  if (inputValue) {
    price = inputValue;
  } else {
    price = event.target.textContent;
  }

  const orderData = {
    title: "Donación",
    quantity: 1,
    price: price,
  };

  console.log(orderData);

  try {
    const response = await fetch("http://localhost:3000/create_preference", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(orderData),
    });
    const preference = await response.json();
    createCheckoutButton(preference.id);
  } catch (error) {
    alert("Error al crear la preferencia: " + error);
  }
};

const createCheckoutButton = (preferenceId) => {
  const bricksBuilder = mp.bricks();

  const renderComponent = async () => {
    const objetoMp = document.getElementsByClassName("wallet-button-3fVDUE svelte-30iu5a");
    if (objetoMp.length > 0) {
      while (objetoMp.length > 0) {
        objetoMp[0].parentNode.removeChild(objetoMp[0]);
      }
    }

    window.checkoutButton = await bricksBuilder.create("wallet", "wallet_container", {
        customization: {
            visual: {
                buttonBackground: 'black',

            },
       },
      initialization: {
        preferenceId: preferenceId,
      },
    });
  };

  renderComponent();
};

const buttons = document.getElementsByClassName("welcome_button");

for (let button of buttons) {
  button.addEventListener("click", handleClick);
}