<template>
<v-app id="app">
    <v-app-bar app color="orange" clipped-left>
      <v-app-bar-title>
        <v-toolbar-title class="text-h4 black--text">Slastena</v-toolbar-title>
      </v-app-bar-title>
    </v-app-bar>
    <v-navigation-drawer app dark clipped>
      <MenuContainer />
    </v-navigation-drawer>
    <v-main>
        <v-container fluid>
            <router-view></router-view>
        </v-container>
    </v-main>
</v-app>
</template>

<script>
import MenuContainer from './navbar/MenuContainer.vue'

export default {
    name: 'LayoutApp',
    components: {
        MenuContainer
    }
}
</script>