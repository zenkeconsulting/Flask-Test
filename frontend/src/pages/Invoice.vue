<template>
	<div class="layout-invoice-page">
        <Button type="button" label="Print" icon="pi pi-print" @click="printClick" style="display:block;margin-bottom: 20px; margin-left: 6px;" class="p-button-outlined invoice-button"></Button>
        <div class="grid">
            <div class="col">
                <div class="card" >
                    <div id="invoice-content">
                        <div class="invoice">
                            <div class="invoice-header">
                                <div class="invoice-company flex align-items-center">
                                    <img class="invoice-logo" :src="'layout/images/logo-'+ ($appState.colorScheme === 'light' ? 'dark' : 'light') + '.png'" alt="atlantis-layout"/>
                                    <img class="invoice-appname" :src="'layout/images/appname-'+ ($appState.colorScheme === 'light' ? 'dark' : 'light') + '.png'" alt="atlantis-layout"/>
                                </div>
                                <div class="ml-2">
                                    <div class="customer-id">Customer ID: C1613</div>
                                    <div class="invoice-address">9137 3rd Lane California City CA 93504, U.S.A.</div>
                                </div>
                            </div>

                            <div class="invoice-to">
                                <div class="invoice-date">29 January, 2021</div>
                                <div class="invoice-id">Invoice <span>#00002</span></div>
                                <div class="invoice-to-name">Customer Firm name</div>
                                <div class="invoice-to-info">
                                    <div>Claire Williams, 148 Hope Lane</div>
                                    <div>Palo Alto, CA 94304. </div>
                                </div>
                            </div>

                            <div class="invoice-items">
                                <table>
                                    <thead>
                                    <tr>
                                        <th>Description</th>
                                        <th>Quantity</th>
                                        <th>Unit Price</th>
                                        <th>Line Total</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr>
                                        <td>Green T-Shirt</td>
                                        <td>1</td>
                                        <td>$49.00</td>
                                        <td>$49.00</td>
                                    </tr>
                                    <tr>
                                        <td>Game Controller</td>
                                        <td>2</td>
                                        <td>$99.00</td>
                                        <td>$198.00</td>
                                    </tr>
                                    <tr>
                                        <td>Mini Speakers</td>
                                        <td>1</td>
                                        <td>$85.00</td>
                                        <td>$85.00</td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>

                            <div class="invoice-summary">
                                <table>
                                    <tbody>
                                    <tr>
                                        <td>Sub total:</td>
                                        <td>$232,00</td>
                                    </tr>
                                    <tr>
                                        <td>Vat:</td>
                                        <td>$00,00</td>
                                    </tr>
                                    <tr>
                                        <td>Total:</td>
                                        <td>$232,00</td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>

                            <div class="invoice-notes">
                                <div>Note: </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
	data() {
		return {
			billData: [
				{
					'billTo': 'TOYOKSU SYSCOM CORPORATION 11-27, MEIEKI 4-CHROME NAKAMURA-KU, NAGOYA 450-0002 JAPAN',
					'date': '30/08/2021',
					'no': 'A/3100',
					'notes': 'N/A'
				}
			],
			billCols: [
				{ field: 'billTo', header: 'BILL TO' },
				{ field: 'date', header: 'DATE' },
				{ field: 'no', header: 'INVOICE NO' },
				{ field: 'notes', header: 'NOTES' }
			],
			productData: [
				{
					'description': 'License A',
					'quantity': '4',
					'price': '$99.00',
					'total': '$396.00'
				},
				{
					'description': 'License B',
					'quantity': '1',
					'price': '$790.00',
					'total': '$790.00'
				},
				{
					'description': 'License C',
					'quantity': '2',
					'price': '$59.00',
					'total': '$118.00'
				}
			],
			productCols: [
				{ field: 'description', header: 'DESCRIPTION' },
				{ field: 'quantity', header: 'QUANTITY' },
				{ field: 'price', header: 'UNIT PRICE' },
				{ field: 'total', header: 'LINE TOTAL' }
			]
		}
	},
	methods: {
		printClick() {
			window.print();
		}
	}
}
</script>

<style scoped>

</style>
