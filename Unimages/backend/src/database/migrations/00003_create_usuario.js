
exports.up = function (knex) {
    return knex.schema.createTable('pessoa', (table) => {
        table.increments('id').primary();
        table.string('email').notNullable().unique();
        table.string('nome').notNullable();
        table.string('senha').notNullable();
    });
};

exports.down = function (knex) {
    return knex.schema.dropTable('pessoa');
};
