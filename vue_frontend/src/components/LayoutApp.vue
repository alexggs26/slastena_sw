<template>
<v-app id="app">
    <v-app-bar app color="orange" clipped-left>
      <v-app-bar-title>
        <v-toolbar-title class="text-h4 black--text"
        style="width:15em"
        >
        Сластена
      </v-toolbar-title>
      </v-app-bar-title>
      <v-layout align-end justify-end>
      <v-btn class="material-icons" @click="logout">
            Выйти из системы
      </v-btn>
      </v-layout>
    </v-app-bar>
    <v-navigation-drawer app color="accent" light clipped>
      <MenuContainer />
    </v-navigation-drawer>
    <v-main>
        <v-container fluid>
            <router-view>></router-view>
        </v-container>
    </v-main>
</v-app>
</template>

<script>
import MenuContainer from './navbar/MenuContainer.vue'

export default {
    name: 'LayoutApp',
    components: {
        MenuContainer,
    },
    methods: {
      logout () {
        this.$store
        .dispatch('logout')
        .then(() => this.$router.push('/login'))
        .catch(err => console.log(err))
      }
    }
}
</script>