module.exports = {
    development: {
        client: 'postgresql',
        connection: {
            // TODO change to your db name
            database: 'unimages',

            // change to your db user
            user: 'jvac99',
            password: '2611',
        },
        pool: {
            min: 2,
            max: 10,
        },
        migrations: {
            tableName: 'knex_migrations',
        },
    },
};

// https://knexjs.org/