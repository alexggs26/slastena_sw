import axios from 'axios'


const store = {
    state: {
        status: '',
        users: []
    },
    getters: {
        USERS: state => {
            return state.users
        }
    },
    mutations: {
        setUsers(state, data) {
            state.status = 'ok'
            state.users = data
        }
    },
    actions: {
        getUsers({ commit }) {
            return new Promise((resolve, reject) => {
                commit('loadRequest')
                axios({
                    url: `${process.env.VUE_APP_BACKEND_HOST}/api/get_all_users/`,
                    method: 'GET'
                })
                .then(resp => {
                    commit('setUsers', resp.data.items)
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