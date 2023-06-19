<template>
    <v-container>
    <v-toolbar flat color="white">
        <v-toolbar-title v-if="this.$route.path !== '/app/orders/create'">
            Заказ № {{ this.mutableOrders[0].meta_order_id }} 
            от {{ this.mutableOrders[0].created_at.substring(0, 10) }}</v-toolbar-title>
        <v-toolbar-title v-if="this.$route.path === '/app/orders/create'">Новый заказ</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="primary" dark class="mr-2" @click="save">Сохранить</v-btn>
        <v-btn color="primary" dark class="mr-2" @click="close">Закрыть</v-btn>
        <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }" v-if="this.$route.path !== '/app/orders/create'">
                <v-btn color="red" dark class="mr-2" v-on="on">Удалить</v-btn>
            </template>
            <v-card>
                <v-card-title class="p-1">
                    Вы действительно хотите удалить всю информацию о заказе?
                </v-card-title>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" flat @click="closeDialog">Закрыть</v-btn>
                    <v-btn color="red" flat @click="deleteAll">Удалить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-toolbar>
    <v-card outlined>
    <v-card-text>
        <v-card-subtitle>
            Общая информация
        </v-card-subtitle>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-autocomplete
                        v-model="mutableOrders[0].provider_id"
                        :items="providers"
                        item-value="id"
                        item-text="title"
                        label="Поставщик"
                        return-object
                        required
                    ></v-autocomplete>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-autocomplete
                        v-model="mutableOrders[0].created_by"
                        :items="users"
                        item-value="id"
                        item-text="full_name"
                        label="Ответственный"
                        return-object
                        required
                    ></v-autocomplete>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>
        </v-card>
        <v-card outlined>
        <v-card-text>
        <v-card-subtitle>
            Товары
            <v-icon small @click="addItem">
                mdi-plus
            </v-icon>
        </v-card-subtitle>
        </v-card-text>
        </v-card>
    <v-container grid-list-md>
        <v-layout wrap v-for="order in mutableOrders" :key="order.id">
            {{ order }}
        <v-flex xs12 sm6 md4>
                    <v-autocomplete
                    v-model="order.name"
                    :items="nomenclature"
                    item-value="id"
                    item-text="name"
                    label="Наименование"
                    return-object
                    required
                ></v-autocomplete>
                </v-flex>
                <v-flex xs12 sm6 md4>
                    <v-text-field v-model="order.wholesale_price" label="Цена закупки"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                    <v-text-field v-model="order.purchase_quantity" label="Количество"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                    <v-text-field :readonly=true label="Сумма">{{ order.purchase_quantity * order.wholesale_price }}</v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                    <v-text-field v-model="order.created_at" :readonly=true label="Дата создания"></v-text-field>
                </v-flex>
            </v-layout>
    </v-container>
    </v-container>
    
</template>

<script>
export default {
    name: 'OrderContainer',
    data: () => ({
        dialog: false,
        newOrderItem: {
            id: 0,
            name: '',
            provider_id: {
                id: 0,
                title: '',
                date_create: ''
            },
            purchase_quantity: 0,
            wholesale_price: 0,
            created_by: {
                id: 0,
                first_name: '',
                last_name: '',
                full_name: '',
                email: '',
            },
            created_at: '',
            uopdated_at: ''
        },
        deletedOrderItems: []
    }),
    computed: {
        isLoggedIn: function() {return this.$store.getters.isLoggedIn},
        curDate () {
            const curDateUnix = new Date(Date.now())
            const curDate = curDateUnix.toLocaleString("default", {year: "numeric"}) + '-' + curDateUnix.toLocaleString("default", {month: "2-digit"}) + '-' + curDateUnix.toLocaleString("default", {day: "2-digit"})
            return curDate
        },
        orders () {
            if (this.$route.path !== '/app/orders/create') {
                return this.$store.getters.ORDERS
            }
            else {
                const orders = [{
                    id: 0,
                    name: '',
                    provider_id: '',
                    purchase_quantity: 0,
                    wholesale_price: 0,
                    created_by: {
                        id: 0,
                        first_name: '',
                        last_name: '',
                        full_name: '',
                        email: '',
                    },
                    created_at: '',
                    uopdated_at: ''
                }]
                return orders
            }
        },
        usersList () {
            return this.$store.getters.USERS
        },
        users () {
            for (const i of this.usersList) {
                i.full_name = i.first_name + ' ' + i.last_name
            }
            return this.usersList
        },
        providers () {
            return this.$store.getters.PROVIDER
        },
        nomenclature () {
            return this.$store.getters.NOMENCLATURE
        },
        mutableOrders () {
              for (const i of this.orders) {
                for (const j of this.users) {
                    if (i.created_by === j.id) {
                        i.created_by = j
                    }
                }
            }
            for (const k of this.orders) {
                for (const l of this.providers) {
                    if (k.provider_id === l.id) {
                        k.provider_id = l
                    }
                }
            }
            for (const x of this.orders) {
                for (const y of this.nomenclature) {
                    if (x.name === y.name) {
                        x.name = y
                    }
                }
            }
            return this.orders
        },
    },

    created () {
        this.$store.dispatch('getNomenclature').then(() => {
            this.$store.dispatch('getUsers').then(() => {
                this.$store.dispatch('getProviderList').then(()=>{
                    if (this.$route.path !== '/app/orders/create')  {
                        let metaOrderId = this.$route.params.metaOrderId
                        this.$store.dispatch('getOrders', { metaOrderId })
                    }
                })
            })
        })
    
    },

    mounted () {
        console.log(this.nomenclature)
        console.log(this.mutableOrders)
    },

    methods: {
        save () {
            // let created_by = this.mutableProvider.created_by.id
            // delete this.mutableProvider.created_by
            // delete this.mutableProvider.created_at
            // delete this.mutableProvider.updated_at
            // this.mutableProvider.created_by = created_by

            // let provider = this.mutableProvider
            // let requisits = this.requisits
            // let contacts = this.contacts
            // let deletedContacts = this.deletedContacts

            // if (this.$route.path !== '/app/providers/create')  {
            //     this.$store.dispatch('updateProvider', { provider })
            //     this.$store.dispatch('updateRequisits', { requisits })
            //     for (const contact of contacts) {
            //         if (contact.id !== undefined) {
            //             this.$store.dispatch('updateContacts', { contact })
            //         }
            //         else {
            //             this.$store.dispatch('createContacts', { contact })
            //         }
            //     for (const deletedContact of deletedContacts) {
            //         if (deletedContact.id !== undefined) {
            //             this.$store.dispatch('deleteContacts', { deletedContact })
            //         }
            //     }
            // }
            // }
            // else {
            //     this.$store.dispatch('createProvider', { provider })
            //     this.$store.dispatch('createRequisits', { requisits })
            //     for (const contact of this.contacts) {
            //         this.$store.dispatch('createContacts', { contact })
            //     }
            // }
        },
        close () {
            this.$router.push('/app/orders/')
        },
        deleteAll () {
            // let provider = this.mutableProvider
            // let requisits = this.requisits
            // let contacts = this.contacts

            // if (this.$route.path !== '/app/providers/create')  {
            //     this.$store.dispatch('deleteProvider', { provider })
            //     this.$store.dispatch('deleteRequisits', { requisits })
            //     for (const contact of contacts) {
            //         if (contact.id !== undefined) {
            //             this.$store.dispatch('deleteContacts', { contact })
            //         }
            //     }
            // }
            // else {
            //     this.$router.push('/app/providers/')
            // }
            // this.$router.push('/app/providers/')
        },    
        closeDialog() {
            this.dialog = false
        },
        addItem () {
            this.orders.push(this.newOrderItem)
        },
        removeItem (item) {
            this.deletedOrderItems.push(item)
            this.orders.splice(this.orders.indexOf(item), 1)
        }
    }
}
</script>