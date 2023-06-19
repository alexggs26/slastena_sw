<template>
    <v-container>
        <v-card class="mx-auto" width="256" tile>
            <v-list nav dense>
                <v-list-item-group>
                    <v-list-item 
                    @click="$router.push({path: '/app/orders' })"
                    >
                        <v-list-item-icon>
                            <v-icon>mdi-approximately-equal-box</v-icon>
                        </v-list-item-icon>
                    Заказы
                    </v-list-item>
                    <v-list-item
                    @click="$router.push({path: '/app/providers' })"
                    >
                        <v-list-item-icon>
                            <v-icon>mdi-badge-account-horizontal</v-icon>
                        </v-list-item-icon>
                    Поставщики
                    </v-list-item>
                   <v-list-item
                    icon="mdi-home"
                    @click="$router.push({path: '/app/nomenclature' })"
                    >
                        <v-list-item-icon>
                            <v-icon>mdi-candy-outline</v-icon>
                        </v-list-item-icon>
                    Товары
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