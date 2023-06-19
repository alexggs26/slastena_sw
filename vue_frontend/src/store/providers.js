import axios from 'axios'


const store = {
    state: {
        status: '',
        provider: [],
        requisits: [],
        contacts: [],
        contact_link: []
    },
    getters: {
        PROVIDER: state => {
            return state.provider
        },
        REQUISITS: state => {
            return state.requisits
        },
        CONTACTS: state => {
            return state.contacts
        }
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
        setContactLink(state, data) {
            state.status = 'ok',
            state.contact_link = data
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
        getRequisits({ commit }, { id }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/requisits/provider_${id}`,
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
        getContacts({ commit }, { id }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/provider_${id}`,
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
        createProvider({ commit }, { provider }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/`,
                    data: provider,
                    method: 'POST'
                })
                    .then(resp => {
                        commit('setProvider', resp.data.item)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        createRequisits({ commit }, { requisits }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/requisits/create/`,
                    data: requisits,
                    method: 'POST'
                })
                    .then(resp => {
                        commit('setRequisits', resp.data.item)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        createContacts({ commit }, { contact }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/create/`,
                    data: contact,
                    method: 'POST'
                })
                    .then(resp => {
                        commit('setContacts', resp.data.item)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        createContactLink({ commit }, { contact_link }) {
            return new Promise((resolve, reject) => {
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/create_link/`,
                    data: contact_link,
                    method: 'POST'
                })
                .then(resp => {
                    commit('commitRequest')
                    resolve(resp)
                })
                .catch(err => {
                    commit('errorRequest')
                    reject(err)
                })
            })
        },
        updateProvider({ commit }, { provider }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/${provider.id}`,
                    data: provider,
                    method: 'PUT'
                })
                    .then(resp => {
                        commit('setProvider', resp.data.item)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        updateRequisits({ commit }, { requisits }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/requisits/provider_${requisits.provider_id}`,
                    data: requisits,
                    method: 'PUT'
                })
                    .then(resp => {
                        commit('setRequisits', resp.data.item)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        updateContacts({ commit }, { contact }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/${contact.id}`,
                    data: contact,
                    method: 'PUT'
                })
                    .then(resp => {
                        commit('setContacts', resp.data.item)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('errorRequest')
                        reject(err)
                    })
            })
        },
        deleteProvider({ commit }, { id }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/${id}`,
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
        deleteRequisits({ commit }, { requisits }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/requisits/provider_${requisits.provider_id}`,
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
        deleteContacts({ commit }, { contact_id }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                console.log(contact_id)
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/${contact_id}`,
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
        },
        deleteContactLink({ commit }, { contact_link }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/providers/contacts/delete_link/`,
                    data: contact_link,
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
        },
    }
}

export default store