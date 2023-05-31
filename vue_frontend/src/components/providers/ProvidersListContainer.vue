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
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark class="mb-2" v-on="on">Добавить поставщика</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
  
            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.title" label="Название"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.date_create" label="Дата создания"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.responsible" label="Ответственный"></v-text-field>
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
          <td>{{ item.created_by }}</td>
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
          providers:[],
          editedIndex: -1,
          editedItem: {
            title: '',
            date_create: '',
            created_by: ''
          },
          defaultItem: {
            title: '',
            date_create: '',
            created_by: '',
          },
        }
    },
  
      computed: {
          isLoggedIn : function() {return this.$store.getters.isLoggedIn},
          formTitle () {
              return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
          }
      },
  
      watch: {
        dialog (val) {
          val || this.close()
        }
      },

      mounted () {
        this.$store.dispatch('getProviderList')
        this.providers = this.$store.state.providers.provider
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
  
        deleteItem (item) {
          const index = this.providers.indexOf(item)
          confirm('Are you sure you want to delete this item?') && this.providers.splice(index, 1)
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
            Object.assign(this.desserts[this.editedIndex], this.editedItem)
          } else {
            this.providers.push(this.editedItem)
          }
          this.close()
        }
      }
    }
  </script>
  
  