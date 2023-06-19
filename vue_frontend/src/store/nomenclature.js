import axios from 'axios'

const store = {
    state: {
        status: '',
        nomenclature: []
    },
    getters: {
        NOMENCLATURE: state =>  {
            return state.nomenclature
        }
    },
    mutations: {
        setNomenclature(state, data) {
            state.nomenclature = data
        },
        deleteOrders(state) {
            state.status = 'ok'
            state.nomenclature = []
        }
    },
    actions: {
        getNomenclature({ commit }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/nomenclature/`,
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
        updateNomenclature({ commit }, { nomenclature }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/nomenclature/${nomenclature.id}`,
                    data: nomenclature,
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
        createNomenclature({ commit }, { nomenclature }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/nomenclature/`,
                    data: nomenclature,
                    method: 'POST'
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
        deleteNomenclature({ commit }, { nomenclature }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/nomenclature/${nomenclature.id}`,
                    method: 'POST'
                })
                .then(resp => {
                    commit('deleteOrders', resp.data.items)
                    resolve(resp)
                }) 
                .catch(err => {
                    commit('errorRequest')
                    reject(err)
                })
            })
        },
    }
}

export default store