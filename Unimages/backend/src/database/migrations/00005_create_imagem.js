
exports.up = function (knex) {
    return knex.schema.createTable('imagem', (table) => {
        table.increments('id').primary();
        table.foreign('autor_id').references('id').inTable('autor');
        table.string('titulo').notNullable();
        table.string('descricao').notNullable();
        table.decimal('valor').notNullable();
        table.string('link').notNullable().unique();
        table.string('categoria').notNullable();
        table.string('resolucao').notNullable();
        table.string('tipo_acesso').notNullable();
        table.string('formato').notNullable();
    });
};

exports.down = function (knex) {
    return knex.schema.dropTable('imagem');
};
