import express from  "express";
import cors from "cors";
import { MercadoPagoConfig, Preference } from "mercadopago";
import bodyParser from 'body-parser';

const client = new MercadoPagoConfig({ accessToken :"TEST-5847637359045422-060211-379bd7c47361023c7e2c5b1238e4dfea-534720125"});
const app = express();                                                                                      
const port = 3000;

// Configurar cabeceras y cors
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Authorization, X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Request-Method');
  res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
  res.header('Allow', 'GET, POST, OPTIONS, PUT, DELETE');
  next();
});

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded
app.use(cors());
app.use(express.json());

app.listen(port, () => {
    console.log(`Server running on port ${port}`)
})

// Ruta para el endpoint raíz
app.get('/', (req, res) => {
    res.send('Welcome to the API');
  });

app.post('/create_preference', async (req, res) => {
    try{
        console.log("entro al create_preference")
        const body = {
            items: [{
                title : req.body.title,
                quantity : Number(req.body.quantity),
                unit_price : Number(req.body.price), 
                currency_id: "ARS",
            }],
            back_urls: {
                success: "http://localhost:3000/success", 
                failure: "http://localhost:3000/failure",
                pending: "http://localhost:3000/pending",
            },
            auto_return: "approved",
        };
        console.log("entro al create_preference2")
        const preference = await Preference(client); 
        console.log("entro al create_preference3"); 
        const result = await preference.create({body});
        console.log("entro al create_preference4")
        res.json({id : result.id})
    }catch{
        console.log("Error al crear la preferencia aca no se que paso");
        res.status(500).send("Error al crear la preferencia aca no se que paso");
    }
});