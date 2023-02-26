<template>
    <v-container fluid fill-height>
         <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
                <v-card class="elevation-12">
                    <v-toolbar dark color="orange accent-3">
                        <v-toolbar-title>Регистрация в Slastena</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <form ref="form" @submit.prevent="register()">
                            <v-text-field
                                v-model="first_name"
                                label="Имя"
                                required
                                hide-details="auto"
                            ></v-text-field>
                            <v-text-field
                                v-model="last_name"
                                label="Фамилия"
                                required
                                hide-details="auto"
                            ></v-text-field>
                            <v-text-field
                                v-model="email"
                                label="E-mail"
                                required
                                hide-details="auto"
                            ></v-text-field>
                            <v-text-field
                                v-model="password"
                                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.required, rules.min]"
                                :type="show1 ? 'text' : 'password'"
                                label="Пароль"
                                name="input-10-1"
                                required
                                @click:append="show1 = !show1"
                                hide-details="auto"
                            ></v-text-field>
                            <!-- <v-text-field
                                v-model="password_confirmation"
                                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.mismatchPasswords]"
                                :type="show1 ? 'text' : 'password'"
                                label="Повторите пароль"
                                name="input-10-1"
                                required
                                @click:append="show1 = !show1"
                                hide-details="auto"
                            ></v-text-field> -->
                            <v-card-actions class="py-0">
                            <v-btn
                                class="mt-4"
                                color="deep-orange darken-2"
                                text
                                @click="register"
                            >
                                Зарегистрироваться
                            </v-btn>
                            <v-spacer></v-spacer>
                            <div class="mt-4 text-end red--text">Уже зарегистрированы?</div>
                            <v-btn
                                class="mt-4"
                                color="deep-orange darken-2"
                                text
                                @click="toLogin"
                            >
                                Авторизация
                            </v-btn>
                            </v-card-actions>
                        </form>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>

export default {
    name: 'RegisterContainer',
    data() {
        return {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            password_confirmation: '',
            show1: false,
            rules: {
                required: value => !!value || 'Введите пароль',
                min: v => v.length >= 6 || 'Минимум 6 символолов',
                emailMatch: () => (`The email and password you entered don't match`),
                // mismatchPasswords: value => value != this.password || 'Пароли не совпадают',
        },

        }
    },
    methods: {
        register () {
            const data = {
                first_name: this.first_name,
                last_name: this.last_name,
                email: this.email,
                password: this.password,
                password_confirmation: this.password_confirmation,
            }
            this.$store
            .dispatch('registration', data)
            .then(() => this.$router.push('/login'))
            .catch(err => console.log(err))
        },
        toLogin () {
            this.$router.push('/login')
        }
    }
}
</script>