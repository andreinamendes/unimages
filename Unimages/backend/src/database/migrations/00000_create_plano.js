
exports.up = function (knex) {
    return knex.schema.createTable('plano', (table) => {
        table.increments('id').primary();
        table.string('descricao').notNullable();
        table.decimal('duracao').notNullable();
        table.decimal('valor').notNullable();
        table.decimal('pix').notNullable();
    });
};

exports.down = function (knex) {
    return knex.schema.dropTable('plano');
};
