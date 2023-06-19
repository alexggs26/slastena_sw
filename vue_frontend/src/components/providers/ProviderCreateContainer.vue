<template>
    <v-container>
    <v-toolbar flat color="white">
        <v-toolbar-title>Добавить нового поставщика</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="primary" dark class="mr-2" @click="save">Сохранить</v-btn>
        <v-btn color="primary" dark class="mr-2" @click="close">Закрыть</v-btn>
    </v-toolbar>
    <v-card outlined>
    <v-card-text>
        <v-card-subtitle>
            Общая информация
        </v-card-subtitle>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="mutableProvider.title" label="Название"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="mutableProvider.date_create" label="Дата создания"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-autocomplete
                        v-model="mutableProvider.created_by"
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
            Реквизиты
        </v-card-subtitle>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="requisits.address" label="Адрес"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="requisits.inn" label="ИНН"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="requisits.ogrn" label="ОГРН"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="requisits.bank_name" label="Банк"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="requisits.bank_bik" label="БИК"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="requisits.bank_account" label="Счет"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="requisits.bank_cors_account" label="Корреспондентский счет"></v-text-field>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>
        </v-card>
        <v-card outlined>
        <v-card-text>
        <v-card-subtitle>
            Контакты
        </v-card-subtitle>
        <v-btn color="primary" dark class="mr-2" @click="addContact()">Добавить контакт</v-btn>
              <v-container grid-list-md>
                <v-layout wrap>
                    <v-flex md4 v-for="contact in contacts" :key="contact.onPageIndex">
                        <v-card class="card-container" flat append-icon="mdi-close">
                            <v-card-text>
                            <v-card-text> {{ contact.onPageIndex }} </v-card-text>
                                <v-divider class="ml-15" vertical></v-divider>
                                <v-btn class="m-10" small @click="deleteContact(contact)">Удалить</v-btn>
                                <v-text-field v-model="contact.first_name" label="Имя"></v-text-field>
                                <v-text-field v-model="contact.last_name" label="Фамилия"></v-text-field>
                                <v-text-field v-model="contact.phone" label="Номер телефона"></v-text-field>
                                <v-text-field v-model="contact.email" label="Электронная почта"></v-text-field>
                                <v-text-field v-model="contact.birthday_date" label="День рождения"></v-text-field>
                                <v-text-field v-model="contact.description" label="Примечание"></v-text-field>
                            </v-card-text>
                        </v-card>
                    </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
export default {
    name: 'ProviderCreateContainer',
    data: () => ({
        dialog: false,
        createdContacts: [],
        deletedContacts: [],
        mutableProvider: {
            title: '',
            date_create: '',
            created_by: {}
        },
        requisits: {},
        contacts: [],
        newContact: {
            onPageIndex: 0,
            first_name: '',
            last_name: '',
            phone: '',
            email: '',
            birthday_date: '',
            description: '',

        },
    }),
    computed: {
        isLoggedIn: function() {return this.$store.getters.isLoggedIn},
        usersList () {
            return this.$store.getters.USERS
        },
        users () {
            for (const i of this.usersList) {
                i.full_name = i.first_name + ' ' + i.last_name
            }
            return this.usersList
        },
       
    },

    mounted () {
        this.$store.dispatch('getUsers')
        const curDate = new Date(Date.now())
        this.mutableProvider.date_create = curDate.toLocaleString("default", {year: "numeric"}) + '-' + curDate.toLocaleString("default", {month: "2-digit"}) + '-' + curDate.toLocaleString("default", {day: "2-digit"});
        },

    methods: {
        save () {
            let created_by = this.mutableProvider.created_by.id
    
            delete this.mutableProvider.created_by
            delete this.mutableProvider.created_at
            delete this.mutableProvider.updated_at

            this.mutableProvider.created_by = created_by

            let provider = this.mutableProvider

            this.$store.dispatch('createProvider', { provider })
              .then(() => {
                let provider_id = this.$store.getters.PROVIDER.id
                let requisits = this.requisits
                requisits.provider_id = provider_id
                requisits.created_by = created_by
                this.$store.dispatch('createRequisits', { requisits })
                .then(() => {
                  for (const contact of this.contacts) {
                    delete contact.onPageIndex
                      this.$store.dispatch('createContacts', { contact })
                      .then(() => {
                        let contact_id = this.$store.getters.CONTACTS.id
                        let contact_link = {provider_id: provider_id, contact_id: contact_id}
                        this.$store.dispatch('createContactLink', { contact_link })
                      })
                        .then(() => {
                          this.$router.push(`/app/providers/details/${provider_id}`)
                        })
                    }
                })
            })
        },
        close () {
            this.$router.push('/app/providers/')
        },

        addContact () {
            this.newContact = Object.assign({}, this.newContact)
            this.newContact.onPageIndex = this.contacts.length + 1
            this.contacts.push(this.newContact)
        },
        deleteContact (removedContact) {
            this.deletedContacts.push(removedContact)
            const index = this.contacts.indexOf(removedContact)
            this.contacts.splice(index, 1)
        },
        closeDialog() {
            this.dialog = false
        }
    }
}
</script>