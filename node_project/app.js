// importando FW
const express = require('express')

// instanciando app
const app = express()
// definindo porta
const port = 3000

// get para route principal
app.get('/', (req, res) => {
    res.send('Imagen node/express ON!')
})

// indicando porta utilizada
app.listen(port, () => {
    console.log(`Executando na porta: ${port}.`)
})