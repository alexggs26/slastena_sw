<template>
    <v-container>
        <v-row :align="align" no-gutters>
            <v-col>
                <v-card class="pa-2" outlined tile>
                    <v-card-title>Съедено конфет</v-card-title>
                    <v-card-text>7 978 263</v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card class="pa-2" outlined tile>
                    <v-card-title>Поглажено котиков</v-card-title>
                    <v-card-text>265</v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card class="pa-2" outlined tile>
                    <v-card-title>Выпито кружек чая</v-card-title>
                    <v-card-text>3 768</v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card class="pa-2" outlined tile>
                    <v-card-title>Уровень сытости Пусиша</v-card-title>
                    <v-card-text>23%</v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card class="pa-2" outlined tile>
                    <v-card-title>Нужно пачек Шебы с креветками</v-card-title>
                    <v-card-text>904</v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card class="pa-2" outlined tile>
                    <v-card-title>Нужно съесть конфет</v-card-title>
                    <v-card-text>2 452 678</v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row>

        </v-row>
    </v-container>
</template>


<script>


export default {
    name: 'MainContainer',
    components: {},
    data() {
        return {

        }
    },
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
    },
    methods: {
      logout: function () {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
      }
    },
}
</script>


<style>

</style>