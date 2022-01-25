
exports.up = function (knex) {
    return knex.schema.createTable('incidents', function (table) {
        table.foreign('pessoa_id').references('id').inTable('ongs');
        table.foreign('ong_id').references('id').inTable('ongs');
    });
};

exports.down = function (knex) {

};
