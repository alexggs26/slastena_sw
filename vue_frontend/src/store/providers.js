import axios from 'axios'


const store = {
    state: {
        status: '',
        provider: [],
        requisits: [],
        contacts: []
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
            state.status = 'ok',
            state.provider = data
        },
        setRequisits(state, data) {
            state.status = 'ok',
            state.requisits = data
        },
        setContacts(state, data) {
            state.status = 'ok',
            state.contacts = data
        },
        deleteProvider(state) {
            state.status = 'deleted provider',
            state.provider = {}
        },
        deleteRequisits(state) {
            state.status = 'deleted requisits',
            state.requisits = {}
        },
        deleteContacts(state) {
            state.status = 'deleted contacts',
            state.contacts = []
        }
    },
    actions: {
        getProviderList({ commit }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
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
                commit('loadRequest')
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
                commit('loadRequest')
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
                commit('loadRequest')
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
        createProvider({ commit }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/`,
                    method: 'POST'
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
        createRequisits({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/requisits/provider_${data.provider.id}`,
                    data: data,
                    method: 'POST'
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
        createContacts({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/provider_${data.provider.id}`,
                    data: data,
                    method: 'POST'
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
        updateProvider({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/${data.provider.id}`,
                    data: data,
                    method: 'PUT'
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
        updateRequisits({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/requisits/provider_${data.provider.id}`,
                    data: data,
                    method: 'PUT'
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
        updateContacts({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/provider_${data.provider.id}`,
                    data: data,
                    method: 'PUT'
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
        deleteProvider({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/${data.provider.id}`,
                    method: 'DELETE'
                })
                    .then(resp => {
                        commit('deleteProvider')
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        deleteRequisits({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/requisits/provider_${data.provider.id}`,
                    method: 'DELETE'
                })
                    .then(resp => {
                        commit('deleteRequisits')
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        deleteContacts({ commit }, { data }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/provider_${data.provider.id}`,
                    method: 'DELETE'
                })
                    .then(resp => {
                        commit('deleteContacts')
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        }
    }
}

export default store