<template>
  <div>
    <v-toolbar flat color="white">
      <v-toolbar-title>Заказы</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Поиск"
          single-line
          hide-details
        ></v-text-field>
      <v-dialog v-model="dialog" max-width="500px">
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark class="mb-2" v-on="on">Добавить заказ</v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">{{ formTitle }}</span>
          </v-card-title>

          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.name" label="Наименование товара"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.wholesale_price" label="Цена закупки"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.amount" label="Сумма"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.provider_name" label="Поставщик"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.created_at" label="Дата создания"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.created_by" label="Ответственный"></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click="close">Закрыть</v-btn>
            <v-btn color="blue darken-1" flat @click="save">Сохранить</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="mutableOrders"
      :search="search"
      class="elevation-1"
    >
    <template v-slot:body="{ items }">
      <tbody>
      <tr v-for="item in items" :key="item.name">
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.wholesale_price }}</td>
        <td>{{ item.amount }}</td>
        <td>{{ item.purchase_quantity }}</td>
        <td>{{ item.provider_id.title }}</td>
        <td>{{ item.created_at.substring(0, 10) }}</td>
        <td>{{ item.created_by.full_name }}</td>
        <td class="justify-center layout px-0">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
      </td>
    </tr>
    </tbody>
    </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>

  export default {
    name: 'MainContainer',
    data: () => ({
      dialog: false,
      search: '',
      headers: [
        {
          text: 'ID',
          align: 'left',
          value: 'id'
        },
        { text: 'Наименование товара', value: 'name' },
        { text: 'Цена закупки', value: 'wholesale_price' },
        { text: 'Сумма', value: 'amount' },
        { text: 'Количество', value: 'purchase_quantity'},
        { text: 'Поставщик', value: 'provider_name'},
        { text: 'Дата создания', value: 'created_at'},
        { text: 'Ответственный', value: 'created_by'},
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      editedIndex: -1,
      editedItem: {
        name: '',
        wholesale_price: 0.00,
        amount: 0.00,
        purchase_quantity: 0,
        provider_name: '',
        created_at: '',
        created_by: ''
      },
      defaultItem: {
        name: '',
        wholesale_price: 0.00,
        amount: 0.00,
        purchase_quantity: 0,
        provider_name: '',
        created_at: '',
        created_by: ''
      },
    }),

    computed: {
        isLoggedIn : function(){ return this.$store.getters.isLoggedIn},
        formTitle () {
            return this.editedIndex === -1 ? 'Добавить заказ' : 'Редактировать заказ'
        },
        orders () {
          return this.$store.getters.ORDERS
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
              for (const l of this.orders) {
                for (const k of this.providers)
                  if (l.provider_id === k.id) {
                      l.provider_id = k
                  }
              }
              return this.orders
        },
    },

    watch: {
      dialog (val) {
        val || this.close()
      }
    },

    created () {
      this.$store.dispatch('getUsers').then(() => {
        this.$store.dispatch('getOrdersList').then(() => {
          this.$store.dispatch('getProviderList')
        })
      })
    },

    methods: {
        logout: function () {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
      },

      editItem (item) {
        this.$router.push(`/app/orders/details/${item.id}`)
      },

      deleteItem (item) {
        const index = this.orders.indexOf(item)
        confirm('Вы уверены, что хотите удалить данные?') && this.orders.splice(index, 1)
      },

      close () {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.orders[this.editedIndex], this.editedItem)
        } else {
          this.orders.push(this.editedItem)
        }
        this.close()
      }
    }
  }
</script>

