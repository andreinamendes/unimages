
exports.up = function (knex) {
    return knex.schema.createTable('assinante', (table) => {
        table.increments('id').primary();
        table.string('descricao').notNullable();
        table.decimal('duracao').notNullable();
        table.decimal('valor').notNullable();
    });
};

exports.down = function (knex) {
    return knex.schema.dropTable('assinante');
};
