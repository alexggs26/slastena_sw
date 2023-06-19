<template>
    <v-app id="app">
      <router-view />
    </v-app>
</template>

<script>
import axios from 'axios'
import router from './router'
import store from './store'

export default {
  name: 'App',
  created: function () {
      axios.interceptors.response.use(function (response) {
        return response
      }, function (error) {
        if (error.response.status === 401) {
          store.dispatch('logout')
          router.push('/login')
        }
        return Promise.reject(error)
      })
  }
};
</script>
