var express = require('express');

const router = express.Router();

/*
const AssinanteController = require('./controllers/AssinanteController');
const AutorController = require('./controllers/AutorController');
const ImagemController = require('./controllers/ImagemController');
const PessoaController = require('./controllers/PessoaController');
const PlanoController = require('./controllers/PlanoController');
*/

router.get('/', (require, response) => {
    return response.json({ message: 'Olá' });
});

/*
router.get('/assinante', AssinanteController.index);
router.get('/autor', AutorController.index);
router.get('/imagem', ImagemController.index);
router.get('/pessoa', PessoaController.index);
router.get('/incidents', PlanoController.index);

router.post('/assinante', AssinanteController.create);
router.post('/autor', AutorController.create);
router.post('/imagem', ImagemController.create);
router.post('/pessoa', PessoaController.create);
router.post('/incidents', PlanoController.create);

router.delete('/assinante/:id', AssinanteController.delete);
router.delete('/autor/:id', AutorController.delete);
router.delete('/imagem/:id', ImagemController.delete);
router.delete('/pessoa/:id', PessoaController.delete);
router.delete('/incidents/:id', PlanoController.delete);
*/

module.exports = router;

// https://expressjs.com/pt-br/
// https://www.alura.com.br/artigos/utilizando-export-modules-no-node-js