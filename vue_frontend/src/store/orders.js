import axios from 'axios'

const store = {
    state: {
        status: '',
        orders: []
    },
    getters: {
        ORDERS: state => {
            return state.orders
        }
    },
    mutations: {
        setOrders(state, data) {
            state.orders = data
        },
        deleteOrders(state) {
            state.status = 'deleted orders',
            state.orders = []
        }
    },
    actions: {
        getOrdersList({ commit }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/orders/`,
                    method: 'GET'
                })
                    .then(resp => {
                        commit('setOrders', resp.data.items)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        getOrders({ commit }, { metaOrderId }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/orders/${metaOrderId}`,
                    method: 'GET'
                })
                    .then(resp => {
                        commit('setOrders', resp.data.items)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        updateOrders({ commit }, { orders}, { metaOrderId }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/orders/${metaOrderId}`,
                    data: orders,
                    method: 'PUT'
                })
                    .then(resp => {
                        commit('setOrders', resp.data.items)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        deleteOrders({ commit }, { metaOrderId }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/orders/${metaOrderId}`,
                    method: 'DELETE'
                })
                    .then(resp => {
                        commit('deletedOrders')
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
    },
}

export default store