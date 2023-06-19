const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    host: 'localhost',
    port: '9000'
  }
})

// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: [
//     'vuetify'
//   ],
//   devServer: {
//     host: '45.8.99.82',
//     port: '8080'
//   }
// })
