<template>
    <v-container fluid fill-height>
         <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
                <v-card class="elevation-12">
                    <v-toolbar dark color="orange accent-3">
                        <v-toolbar-title>Slastena</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <form ref="form" @submit.prevent="login()">
                            <v-text-field
                                v-model="email"
                                label="Электронная почта"
                                required
                                :rules="[rules.required_email]"
                                hide-details="auto"
                            ></v-text-field>
                            <v-text-field
                                v-model="password"
                                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.required_pw, rules.min]"
                                :type="show1 ? 'text' : 'password'"
                                label="Пароль"
                                name="input-10-1"
                                required
                                @click:append="show1 = !show1"
                                hide-details="auto"
                            ></v-text-field>
                            <v-card-actions class="py-0">
                            <v-btn
                                class="mt-4"
                                color="deep-orange darken-2"
                                text
                                @click="login"
                            >
                                Войти
                            </v-btn>
                            <v-spacer></v-spacer>
                            <div class="mt-4 text-end red--text caption">Еще не зарегистрированы?</div>
                            <v-btn
                                class="mt-4"
                                color="deep-orange darken-2"
                                text
                                @click="toRegister"
                            >
                                Регистрация
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
    name: 'AuthContainer',
    data() {
        return {
            email: '',
            password: '',
            show1: false,
            rules: {
                required_pw: value => !!value || 'Введите пароль',
                required_email: value => !!value || 'Введите Email',
                min: v => v.length >= 6 || 'Минимум 6 символолов',
                emailMatch: () => (`The email and password you entered don't match`),
        },

        }
    },
    methods: {
        login () {
            let email = this.email 
            let password = this.password
            this.$store
            .dispatch('login', { email, password })
            .then(() => this.$router.push('/app/orders'))
            .catch(err => console.log(err))
        },
        toRegister () {
            this.$router.push('register/')
        }
    }  

}
</script>