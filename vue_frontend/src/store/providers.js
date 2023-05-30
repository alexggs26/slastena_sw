import axios from 'axios'


const store = {
    state: {
        status: '',
        provider: {},
        requisits: {},
        contacts: {}
    },
    mutations: {
        loadRequest(state) {
            state.status = 'loading'
        },
        commitRequest(state) {
            state.status = 'ok'
        },
        errorRequest(state) {
            state.status = 'error'
        },
        setProvider(state, data) {
            state.provider = data
        },
        setRequisits(state, data) {
            state.requisits = data
        },
        setContacts(state, data) {
            state.contacts = data
        }
    },
    actions: {
        getProviderList({ commit }) {
            return new Promise((resolve, reject) => {
                commit('load_request')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/`,
                    method: 'GET'
                })
                    .then(resp => {
                        commit('setProvider', resp.data.items)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
                })
        },
        getProvider({ commit }, { id }) {
            return new Promise((resolve, reject) => {
                commit('load_request')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/${id}`,
                    method: 'GET'
                })
                    .then(resp => {
                        commit('setProvider', resp.data.items)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
                })
        },
        getRequisit({ commit }, { provider_id }) {
            return new Promise((resolve, reject) => {
                commit('load_request')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/requisits/provider_${provider_id}`,
                    method: 'GET'
                })
                    .then(resp => {
                        commit('setRequisits', resp.data.items)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        getContact({ commit }, { provider_id }) {
            return new Promise((resolve, reject) => {
                commit('load_request')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/provider_${provider_id}`,
                    method: 'GET'
                })
                    .then(resp => {
                        commit('setContacts', resp.data.items)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        createProvider({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('load_request')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/`,
                    data: data,
                    method: 'POST'
                })
                    .then(resp => {
                        commit('commitRequest')
                    })
            })
        }
    }
}

export default store