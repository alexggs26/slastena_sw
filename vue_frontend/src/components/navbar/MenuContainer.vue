<template>
    <v-container>
        <v-card class="mx-auto" width="256" tile>
            <v-list nav dense>
                <v-list-item-group color="accent">
                    <v-list-item>
                        <router-link to="/main">Главная</router-link>
                    </v-list-item>
                    <v-list-item>
                        <router-link to="/business-process">Поставщики</router-link>
                    </v-list-item>
                    <v-list-item>
                        <router-link to="/sales">Управление заказами</router-link>
                    </v-list-item>
                    <v-list-item>
                        <router-link to="/service">Продажи</router-link>
                    </v-list-item>
                    <v-list-item>
                        <router-link to="/integration">Склад</router-link>
                    </v-list-item>
                    <v-list-item>
                        <router-link to="/warehouse">Отчеты</router-link>
                    </v-list-item>
                    <v-list-item>
                        <router-link to="/finance">Помощь</router-link>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
        </v-card>
    </v-container>
</template>

<script>
export default {
    name: 'MenuContainer',
    data() {
        return {
           
        }
    },
    methods: {

    }
}
</script>

<style>

</style>