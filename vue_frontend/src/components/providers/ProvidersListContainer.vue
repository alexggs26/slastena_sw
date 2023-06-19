<template>
    <div>
      <v-toolbar flat color="white">
        <v-toolbar-title>Поставщики</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Поиск"
          single-line
          hide-details
        ></v-text-field>
        <v-btn color="primary" dark class="mb-2" @click="createItem">Добавить поставщика</v-btn>
      </v-toolbar>
      <v-data-table
        :headers="headers"
        :items="providers"
        :search="search"
        class="elevation-1"
      >
      <template v-slot:body="{ items }">
        <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.title }}</td>
          <td>{{ item.date_create }}</td>
          <td>{{ item.created_by.full_name }}</td>
          <v-dialog v-model="dialog" max-width="500px">   
          <template v-slot:activator="{ on }">
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
              v-on="on"
            >
              mdi-delete
          </v-icon>
          </td>
        </template>
            <v-card>
                <v-card-title class="p-1">
                    Вы действительно хотите удалить всю информацию о поставщике?
                </v-card-title>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" flat @click="closeDialog">Закрыть</v-btn>
                    <v-btn color="red" flat @click="deleteItem(item)">Удалить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
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
      name: 'ProvidersListContainer',
      data: () => {
        return {
          dialog: false,
          search: '',
          headers: [
            { text: 'ID', value: 'id', align: 'left' },
            { text: 'Поставщик', value: 'title' },
            { text: 'Дата создания', value: 'date_create' },
            { text: 'Ответственный', value: 'created_by' },
            { text: 'Действия', value: 'actions', sortable: false },
          ],
          providers: [],
          users: [],
        }
      },
  
      computed: {
          isLoggedIn : function() {return this.$store.getters.isLoggedIn},
      },

      created () {
        this.$store.dispatch('getProviderList').then(() => {
          this.$store.dispatch('getUsers')
        })
      },

      mounted () {
        this.users = this.$store.getters.USERS
        this.providers = this.$store.getters.PROVIDER
        for (const i of this.providers) {
          for (const j of this.users) {
            if (i.created_by === j.id) {
                j.full_name = j.first_name + ' ' + j.last_name
                i.created_by = j
            }
          }
        }
      },
      methods: {
        logout: function () {
          this.$store.dispatch('logout')
          .then(() => {
            this.$router.push('/login')
            })
        },
        
        editItem (item) {
          this.$router.push(`/app/providers/details/${item.id}`)
        },

        createItem () {
          this.$router.push('/app/providers/create')
        },
        deleteItem (item) {
          this.dialog = false
          let id = item.id
          this.$store.dispatch('deleteProvider', { id }).then(() => {
              this.$store.dispatch('getRequisits', { id }).then(() => {
                let requisits = this.$store.getters.REQUISITS[0]
                  this.$store.dispatch('deleteRequisits', { requisits }).then(() => {
                    this.$store.dispatch('getContacts', { id }).then(() => {
                      const contacts = this.$store.getters.CONTACTS
                      for (const i of contacts) {
                        let contact_id = i.id
                        console.log(contact_id)
                        this.$store.dispatch('deleteContacts', { contact_id }).then(() => {
                          let contact_link = {provider_id: id, contact_id: i.id}
                          this.$store.dispatch('deleteContactLink', { contact_link })
                        })
                      }
                }).then(() => {
                        this.$store.dispatch('getProviderList')
                      })
            })
          })
          })
         
        },
        closeDialog() {
            this.dialog = false
        },
      }
    }
  </script>
  
  