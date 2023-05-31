<template>
    <v-container>
    <v-toolbar flat color="white">
        <v-toolbar-title>{{ provider.title }}</v-toolbar-title>
        <v-spacer></v-spacer>
    </v-toolbar>
    <div class="ma-4">
            <v-card
            class="d-flex flex-row mb-6"
            color="grey lighten-4"
            flat
            >
                <v-card-subtitle primary-title>Общая информация</v-card-subtitle>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="provider.title"
                        clearable
                        hide-details="auto"
                        label="Название"
                        ></v-text-field>
                </v-responsive>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                <v-autocomplete
                    v-model="users.id"
                    :items="users"
                    item-value="id"
                    item-text="full_name"
                    return_object
                    label="Ответственный"
                    placeholder="Select..."
                    required
                ></v-autocomplete>
                </v-responsive>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="provider.date_create"
                        clearable
                        hide-details="auto"
                        label="Дата создания"
                        ></v-text-field>
                </v-responsive>
            </v-card>
            <v-card
            class="d-flex flex-row mb-6"
            color="grey lighten-4"
            flat
            >
            <v-card-subtitle primary-title>Реквизиты</v-card-subtitle>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="requisits.address"
                        clearable
                        hide-details="auto"
                        label="Адрес"
                        ></v-text-field>
                </v-responsive>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="requisits.org_type"
                        clearable
                        hide-details="auto"
                        label="Тип организации"
                        ></v-text-field>
                </v-responsive>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="requisits.inn"
                        clearable
                        hide-details="auto"
                        label="ИНН"
                        ></v-text-field>
                </v-responsive>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="requisits.ogrn"
                        clearable
                        hide-details="auto"
                        label="ОГРН"
                        ></v-text-field>
                </v-responsive>
               
            </v-card>   
            <v-card
            class="d-flex flex-row mb-6"
            color="grey lighten-4"
            flat
            >
            <v-card-subtitle primary-title>Банковские реквизиты</v-card-subtitle>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="requisits.bank_name"
                        clearable
                        hide-details="auto"
                        label="Банк"
                        ></v-text-field>
                </v-responsive>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="requisits.bank_bik"
                        clearable
                        hide-details="auto"
                        label="БИК"
                        ></v-text-field>
                </v-responsive>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="requisits.bank_account"
                        clearable
                        hide-details="auto"
                        label="Счет"
                        ></v-text-field>
                </v-responsive>
                <v-responsive
                    class="mx-auto"
                    max-width="344"
                >
                        <v-text-field
                        v-model="requisits.bank_cors_account"
                        clearable
                        hide-details="auto"
                        label="Корреспондентский счет"
                        ></v-text-field>
                </v-responsive>
            </v-card>
        </div>
        <div>
            <v-card-subtitle primary-title>Контакты</v-card-subtitle>
            <v-card>
                    <v-card 
                    v-for="contact in contacts" :key="contact.id"
                    class="d-flex flex-row mb-6"
                    color="grey lighten-4"
                    flat
                    >
                        <v-responsive
                            class="mx-auto"
                            max-width="344"
                        >
                                <v-text-field
                                v-model="contact.first_name"
                                clearable
                                hide-details="auto"
                                label="Имя"
                                ></v-text-field>
                         </v-responsive>
                         <v-responsive
                            class="mx-auto"
                            max-width="344"
                        >
                                <v-text-field
                                v-model="contact.last_name"
                                clearable
                                hide-details="auto"
                                label="Фамилия"
                                ></v-text-field>
                         </v-responsive>
                         <v-responsive
                            class="mx-auto"
                            max-width="344"
                        >
                                <v-text-field
                                v-model="contact.phone"
                                clearable
                                hide-details="auto"
                                label="Телефон"
                                ></v-text-field>
                         </v-responsive>
                         <v-responsive
                            class="mx-auto"
                            max-width="344"
                        >
                                <v-text-field
                                v-model="contact.email"
                                clearable
                                hide-details="auto"
                                label="Эл. почта"
                                ></v-text-field>
                         </v-responsive>
                         <v-responsive
                            class="mx-auto"
                            max-width="344"
                        >
                                <v-text-field
                                v-model="contact.date_bird"
                                clearable
                                hide-details="auto"
                                label="День рождения"
                                ></v-text-field>
                         </v-responsive>
                         <v-responsive
                            class="mx-auto"
                            max-width="344"
                        >
                                <v-text-field
                                v-model="contact.description"
                                clearable
                                hide-details="auto"
                                label="Примечание"
                                ></v-text-field>
                         </v-responsive>
                    </v-card>
                </v-card>
        </div>
    </v-container>
</template>

<script>
export default {
    name: 'ProviderContainer',
    data: () => ({
        provider: {
            id: 0,
            date_create: '',
            title: '',
            created_by: '',
            created_at: '',
            updated_at: ''
        },
        requisits: {},
        contacts: {},
        users: [],
    }),
    computed: {
        isLoggedIn: function() {return this.$store.getters.isLoggedIn},
    },

    mounted () {
        let id = this.$route.params.id
        this.$store.dispatch('getProvider', { id })
        // this.$store.dispatch('getRequisit', { id })
        // this.$store.dispatch('getContact', { id })
        this.$store.dispatch('getUsers')
        this.provider = this.$store.state.providers.provider[0]
        // this.requisits = this.$store.state.providers.requisits[0]
        // this.contacts = this.$store.state.providers.contacts[0]
        this.users = this.$store.state.users.users
        this.users = this.users.map(v => ({...v, full_name: v.first_name + ' ' + v.last_name}))
    },

    methods: {
        
    }
}
</script>