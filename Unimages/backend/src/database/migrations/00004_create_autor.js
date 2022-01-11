
exports.up = function (knex) {
    return knex.schema.createTable('autor', (table) => {
        table.foreign('pessoa_id').references('id').inTable('autor');
        table.string('nome_do_banco').notNullable();
        table.string('agencia').notNullable();
        table.string('numero_da_conta').notNullable().unique();
        table.string('pix').notNullable();
    });
};

exports.down = function (knex) {
    return knex.schema.dropTable('autor');
};