import axios from 'axios'

const token = localStorage.getItem('token')
if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

const store = {
    state: {
        status: '',
        token: localStorage.getItem('token') ?? '',
        user: localStorage.getItem('user') ?? {}
    },
    getters: {
        isLogged: state => !!state.token,
        authStatus: state => state.status,
    },
    mutations: {
        auth_request(state) {
            state.status = 'loading';
        },
        auth_success(state, token, user) {
            state.status = 'success';
            state.token = token;
            state.user = user;
        },
        auth_error(state) {
            state.status = 'error';
        },
        logout(state) {
            state.status = '';
            state.token = '';
        },
    },
    actions: {
        login({ commit }, user) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/login/`,
                    data: user,
                    method: 'POST'
                })
                    .then(resp => {
                        const token = resp.data.token
                        const user = resp.data.user
                        localStorage.setItem('token', token)
                        localStorage.setItem('user', user)
                        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
                        commit('auth_success', token, user)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        localStorage.removeItem('user')
                        reject(err)
                    })
            })
        },
        registration({ commit }, user) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/signup/`,
                    data: user,
                    method: 'POST'
                })
                    .then(resp => {
                        const user = resp.data.user
                        localStorage.setItem('token', token)
                        localStorage.setItem('user', user)
                        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
                        commit('auth_success', token, user)
                        localStorage.removeItem('token')
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        localStorage.removeItem('user')
                        reject(err)
                    })
            })
        }
    },
    modules: {}
}

export default store
