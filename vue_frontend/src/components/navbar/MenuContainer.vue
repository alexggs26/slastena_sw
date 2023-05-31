<template>
    <v-container>
        <v-card class="mx-auto" width="256" tile>
            <v-list nav dense>
                <v-list-item-group>
                    <v-list-item>
                        <router-link to="/app/orders">Заказы</router-link>
                    </v-list-item>
                    <v-list-item>
                        <router-link to="/app/providers">Поставщики</router-link>
                    </v-list-item>
                    <v-list-item>
                        <router-link to="/app/nomenclature">Товары</router-link>
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