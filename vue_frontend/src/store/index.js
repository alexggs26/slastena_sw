import Vue from 'vue'
import Vuex from 'vuex'
import auth from './auth'
import providers from './providers'
import users from './users'
import orders from './orders'
import nomenclature from './nomenclature'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth,
    providers,
    users,
    orders,
    nomenclature
  }
})
