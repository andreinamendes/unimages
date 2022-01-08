var express = require('express');

const router = express.Router();

router.get('/', (require, response) => {
    return response.json({ message: 'Olá' });
});

/*
router.post('/sessions', SessionController.create);
router.get('/ongs', OngController.index);
router.post('/ongs', OngController.create);
router.get('/profile', ProfileController.index);
router.get('/incidents', IncidentController.index);
router.post('/incidents', IncidentController.create);
router.delete('/incidents/:id', IncidentController.delete);
*/

module.exports = router;

// https://expressjs.com/pt-br/
// https://www.alura.com.br/artigos/utilizando-export-modules-no-node-js