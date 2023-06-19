<template>
    <div>
      <v-toolbar flat color="white">
        <v-toolbar-title>Справочник товаров</v-toolbar-title>
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
            <v-btn color="primary" dark class="mb-2" v-on="on">Добавить товар</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
  
            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.name" label="Наименование"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.selling_price" label="Розничная цена продажи"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.created_by" label="Ответственный (g)"></v-text-field>
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
        :items="nomenclature"
        :search="search"
        class="elevation-1"
      >
      <template v-slot:body="{ items }">
        <tbody>
        <tr v-for="item in items" :key="item.name">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.selling_price }}</td>
          <td>{{ item.created_at }}</td>
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
      name: 'NomeclatureListContainer',
      data: () => ({
        dialog: false,
        search: '',
        headers: [
          {
            text: 'ID',
            align: 'left',
            value: 'id'
          },
          { text: 'Наименование', value: 'name' },
          { text: 'Розничная цена продажи', value: 'selling_price' },
          { text: 'Дата создания', value: 'created_at' },
          { text: 'Ответственный', value: 'created_by' },
          { text: 'Действия', value: 'actions', sortable: false },
        ],
        nomenclature: [],
        editedIndex: -1,
        editedItem: {
          name: '',
          selling_price: 0.00,
          created_by: ''
        },
        defaultItem: {
          name: '',
          selling_price: 0.00,
          created_by: ''
        },
      }),
  
      computed: {
          isLoggedIn : function(){ return this.$store.getters.isLoggedIn},
          formTitle () {
              return this.editedIndex === -1 ? 'Новый товар' : 'Редактировать товар'
          }
      },
  
      watch: {
        dialog (val) {
          val || this.close()
        }
      },
  
      created () {
        this.initialize()
      },
  
      methods: {
          logout: function () {
          this.$store.dispatch('logout')
          .then(() => {
            this.$router.push('/login')
          })
        },
        initialize () {
          this.nomenclature = [
            {
              id: 1,
              name: 'Кара-Кум',
              selling_price: '1280',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 2,
              name: 'Тортимилка',
              selling_price: '560',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 3,
              name: 'Петушок',
              selling_price: '780',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 4,
              name: 'Степ',
              selling_price: '550',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 5,
              name: 'Отломи',
              selling_price: '435',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 6,
              name: 'Джек',
              selling_price: '360',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 7,
              name: 'Рот Фронт Батончик',
              selling_price: '710',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 8,
              name: 'Левушка',
              selling_price: '520',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 9,
              name: 'Крокант',
              selling_price: '370',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 10,
              name: 'Юбилейное',
              selling_price: '35',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 11,
              name: 'К чаю',
              selling_price: '150',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 12,
              name: 'Аленка',
              selling_price: '320',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 13,
              name: 'Мишка косолапый',
              selling_price: '980',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 14,
              name: 'Атташе',
              selling_price: '710',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 15,
              name: 'Халва глазированная',
              selling_price: '740',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
            {
              id: 16,
              name: 'Коровка',
              selling_price: '280',
              created_by: 'Петров Михаил',
              created_at: '2023-04-29',
            },
          ]
        },
  
        editItem (item) {
          this.editedIndex = this.nomenclature.indexOf(item)
          this.editedItem = Object.assign({}, item)
          this.dialog = true
        },
  
        deleteItem (item) {
          const index = this.nomenclature.indexOf(item)
          confirm('Вы уверены, что хотите удалить данные?') && this.nomenclature.splice(index, 1)
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
            Object.assign(this.nomenclature[this.editedIndex], this.editedItem)
          } else {
            this.nomenclature.push(this.editedItem)
          }
          this.close()
        }
      }
    }
</script>
  
  