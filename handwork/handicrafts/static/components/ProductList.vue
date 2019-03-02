<template>
    <div>

        <b-breadcrumb :items="items"/>
        <div class="row">
            <div class="col-md-4 product-list grow"
                 v-for="product in products"
                 :key="product.id"
            >
                <a
                        class="card-url"
                        v-bind:href="$hostname + product.get_url"
                >
                    <b-card no-body
                            v-bind:img-src="getImages(product)"
                            img-alt="Image"
                            img-top
                    >
                        <h4 slot="header">{{ product.label }}</h4>
                        <div slot="footer">
                            {{ product.description }}
                            <p><b>{{ product.price }} р.</b></p>
                        </div>
                    </b-card>
                </a>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from "axios";

    export default {
        data() {
            return {
                items: [{
                    text: 'Главная',
                    href: this.$hostname
                }, {
                    text: 'Каталог',
                    href: this.$hostname + '/catalog/'
                }],
                products: [],
            }
        },
        methods: {
            addBreadcrumb(catalog) {
                this.items.push({
                    text: catalog.label,
                    active: true,
                })
            },
            getImages(product) {
                try {
                    return product.images[0].image;
                } catch (e) {
                    return "";
                }
            },
            getProducts() {
                axios.get(this.$hostname_api + this.$pathname).then((res) => {
                    this.products = res.data;
                    this.addBreadcrumb(this.products[0].catalog);
                }).catch(error => console.log(error));
            }
        },
        beforeMount() {
            this.getProducts()
        },
    }
</script>
<style scoped>
    .product-list {
        padding: 10px;
    }

    #main {
        padding: 10px 0px;
    }
</style>
