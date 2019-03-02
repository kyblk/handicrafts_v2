<template>
    <div class="container">
        <div class="col-sm-6 section-title">
            <h2>Каталог</h2>
        </div>
        <div class="row">
            <div class="col-md-4 catalog-list grow"
                 v-for="catalog in catalogs"
                 :key="catalog.id"
            >
                <a
                        class="card-url"
                        v-bind:href="$hostname + catalog.get_url"
                >
                    <b-card no-body
                            v-bind:img-src="catalog.image"
                            img-alt="Image"
                            img-top
                    >
                        <h4 slot="header">{{ catalog.label }}</h4>
                        <div slot="footer">
                            <small class="text-muted">3 шт.</small>
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
                catalogs: [],
            }
        },
        methods: {
            getCatalogs() {
                axios.get(this.$hostname_api + "/catalog/").then(res => this.catalogs = res.data)
                    .catch(error => console.log(error))
            }
        },
        beforeMount() {
            this.getCatalogs()
        },
    }
</script>
<style scoped>

    .catalog-list {
        padding: 10px;
    }

</style>