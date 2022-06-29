<template>
	<div class="layout-dashboard">
		<div class="grid">
			<div class="col-12 md:col-4">
				<div class="card widget-overview-box widget-overview-box-1">
					<span class="overview-title">
						CONVERSATION RATE
					</span>
					<div class="flex justify-content-between">
						<div class="overview-detail flex justify-content-between">
							<div class="overview-badge flex justify-content-center align-items-center">
								<i class="pi pi-arrow-down"></i>
								<span>0.6%</span>
							</div>
							<div class="overview-text">
								0.81%
							</div>
						</div>
					</div>
					<img src="layout/images/dashboard/rate.svg">
				</div>
			</div>
			<div class="col-12 md:col-4">
				<div class="card widget-overview-box widget-overview-box-2">
					<span class="overview-title">
						AVG. ORDER VALUE
					</span>
					<div class="flex justify-content-between">
						<div class="overview-detail flex justify-content-between">
							<div class="overview-badge flex justify-content-center align-items-center">
								<i class="pi pi-arrow-up"></i>
								<span>4,2%</span>
							</div>
							<div class="overview-text">
								$306.2
							</div>
						</div>
					</div>
					<img src="layout/images/dashboard/value.svg">
				</div>
			</div>
			<div class="col-12 md:col-4">
				<div class="card widget-overview-box widget-overview-box-3">
					<span class="overview-title">
						ORDER QUANTITY
					</span>
					<div class="flex justify-content-between">
						<div class="overview-detail flex justify-content-between">
							<div class="overview-badge flex justify-content-center align-items-center">
								<i class="pi pi-minus"></i>
								<span>2,1%</span>
							</div>
							<div class="overview-text">
								1,620
							</div>
						</div>
					</div>
					<img src="layout/images/dashboard/quantity.svg">
				</div>
			</div>

			<div class="col-12 md:col-8">
				<div class="card widget-visitor-graph">
					<div class="card-header">
						<span>Unique visitor graph</span>
						<Dropdown :options="visitorYear" v-model="selectedVisitorYear" optionLabel="name" @change="changeVisitorChart"></Dropdown>
					</div>

					<div class="graph-content grid">
						<div class="col-12 md:col-6">
							<h2>{{growth}}</h2>
							<h6>MRR GROWTH</h6>
							<p>Measure how fast you’re growing mothly recurring revenue. <a href="#">Learn more</a></p>
						</div>
						<div class="col-12 md:col-6">
							<h2>{{avgCustomer}}</h2>
							<h6>AVG. MRR/CUSTOMER</h6>
							<p>The revenue generated per account on a monthly or yearly basis. <a href="#">Learn more</a></p>
						</div>
					</div>

					<div class="graph">
						<h6>Revenue</h6>
						<Chart ref="visitor" type="bar" :data="visitorChart" :options="visitorChartOptions" id="visitor-chart"></Chart>
					</div>
				</div>
			</div>

			<div class="col-12 md:col-4">
				<div class="card widget-timeline">
					<div class="timeline-header flex justify-content-between align-items-center">
						<p>Transaction history</p>
						<div class="header-icons">
							<i class="pi pi-refresh"></i>
							<i class="pi pi-filter"></i>
						</div>
					</div>
					<div class="timeline-content">
						<Timeline :value="timelineEvents" class="custimized-timeline">
							<template #marker="slotProps">
								<span class="custom-marker" :style="{backgroundColor: slotProps.item.iconColor}">
									<i :class="slotProps.item.icon"></i>
								</span>
							</template>
							<template #content="slotProps">
								<div class="flex align-items-center justify-content-between">
									<p>{{slotProps.item.transaction}}</p>
									<h6 :style="{color: slotProps.item.amountColor}">{{slotProps.item.amount}}</h6>
								</div>
								<span>{{slotProps.item.date}}</span>
							</template>
						</Timeline>
					</div>
					<div class="timeline-footer flex align-items-center justify-content-center">
						<a href="#">View all transactions <i class="pi pi-arrow-down"></i></a>
					</div>
				</div>
			</div>

			<div class="col-12 md:col-4">
				<div class="card widget-country-graph">
					<div class="country-title">Country distrubutions</div>
					<div class="country-graph flex justify-content-center">
						<Chart type="doughnut" id="country-chart" :data="countryChart" :options="countryChartOptions" style="position: relative; width: 75%"></Chart>
					</div>
					<div class="country-content">
						<ul>
							<li class="flex justify-content-between align-items-center">
								<div class="flex justify-content-between align-items-center">
									<div class="color" style="background-color: #00D0DE; box-shadow: 0px 0px 10px rgba(0, 208, 222, 0.3);"></div>
									<span>United States of America</span>
								</div>
								<span>25%</span>
							</li>
							<li class="flex justify-content-between align-items-center">
								<div class="flex justify-content-between align-items-center">
									<div class="color" style="background-color: #873EFE; box-shadow: 0px 0px 10px rgba(135, 62, 254, 0.3)"></div>
									<span>China</span>
								</div>
								<span>20%</span>
							</li>
							<li class="flex justify-content-between align-items-center">
								<div class="flex justify-content-between align-items-center">
									<div class="color" style="background-color: #FC6161; box-shadow: 0px 0px 10px rgba(252, 97, 97, 0.3)"></div>
									<span>Japan</span>
								</div>
								<span>17%</span>
							</li>
							<li class="flex justify-content-between align-items-center">
								<div class="flex justify-content-between align-items-center">
									<div class="color" style="background-color: #EEE500; box-shadow: 0px 0px 10px rgba(238, 229, 0, 0.3)"></div>
									<span>Australia</span>
								</div>
								<span>15%</span>
							</li>
							<li class="flex justify-content-between align-items-center">
								<div class="flex justify-content-between align-items-center">
									<div class="color" style="background-color: #EC4DBC; box-shadow: 0px 0px 10px rgba(236, 77, 188, 0.3)"></div>
									<span>India</span>
								</div>
								<span>10%</span>
							</li>
							<li class="flex justify-content-between align-items-center">
								<div class="flex justify-content-between align-items-center">
									<div class="color" style="background-color: #0F8BFD; box-shadow: 0px 0px 10px rgba(15, 139, 253, 0.3)"></div>
									<span>Rusian Federation</span>
								</div>
								<span>8%</span>
							</li>
							<li class="flex justify-content-between align-items-center">
								<div class="flex justify-content-between align-items-center">
									<div class="color" style="background-color: #545C6B"></div>
									<span>Others</span>
								</div>
								<span>5%</span>
							</li>
						</ul>
					</div>
				</div>
			</div>

			<div class="col-12 md:col-8">
				<div class="card widget-revenue-graph">
					<div class="card-header">
						<span>Monthly revenue</span>
						<Dropdown :options="revenueMonth" v-model="selectedRevenueMonth" optionLabel="name" @change="changeRevenueChart($event)"></Dropdown>
					</div>

					<div class="graph">
						<Chart ref="revenue" type="line" id="revenue-chart" :data="revenueChart" :options="revenueChartOptions"></Chart>
					</div>
				</div>
			</div>

			<div class="col-12 md:col-8">
				<div class="card widget-table">
					<div class="card-header">
						<span>Yearly win</span>
						<Dropdown :options="orderYear" v-model="selectedOrderYear" optionLabel="name" @change="recentSales($event)"></Dropdown>
					</div>
					<DataTable ref="dt" :value="customersTable" :selection="selectedCustomers1" dataKey="id" responsiveLayout="scroll"
						:rowHover="true" :rows="10" :paginator="true">
						<Column field="agent" header="Agent" sortable style="min-width: 14rem">
							<template #body="{data}">
								<img :alt="data.representative.name" :src="'demo/images/avatar/' + data.representative.image" width="24" class="mr-2" style="vertical-align: middle" />
								<span class="image-text">{{data.representative.name}}</span>
							</template></Column>
						<Column field="country.name" header="Country" sortable style="min-width: 10rem">
							<template #body="{data}">
								<span class="ml-2" style="vertical-align: middle">{{data.country.name}}</span>
							</template>
						</Column>
						<Column field="date" header="Date" sortable>
							<template #body="{data}">
								{{formatDate(data.date)}}
							</template></Column>
						<Column field="balance" header="Balance" sortable>
							<template #body="{data}">
								{{formatCurrency(data.balance)}}
							</template>
						</Column>
						<Column headerStyle="width: 8em" bodyStyle="text-align: center">
							<template #body>
								<Button class="p-button-text" icon="pi pi-copy"></button>
                                <Button class="p-button-text" icon="pi pi-pencil"></button>
                                <Button class="p-button-text" icon="pi pi-ellipsis-h"></button>
							</template>
						</Column>
					</DataTable>
				</div>
			</div>

			<div class="col-12 md:col-4">
				<div class="card widget-performance">
					<div class="header">
						<span>Quarterly win</span>
						<p class="subtitle">Top performances</p>
					</div>
					<div class="content">
						<ul>
							<li class="person-item">
								<Avatar image="layout/images/dashboard/ann.png" v-badge="1" class="mr-2" shape="circle"></Avatar>
								<div class="person-info">
									<div class="amount">$94,815</div>
									<div class="name">Ann Vaccaro</div>
								</div>
							</li>
							<li class="person-item">
								<Avatar image="layout/images/dashboard/miracle.png" v-badge="2" class="mr-2" shape="circle"></Avatar>
								<div class="person-info">
									<div class="amount">$78,985</div>
									<div class="name">Miracle Aminoff</div>
								</div>
							</li>
							<li class="person-item">
								<Avatar image="layout/images/dashboard/kaylynn.png" v-badge="3" class="mr-2" shape="circle"></Avatar>
								<div class="person-info">
									<div class="amount">$53,611</div>
									<div class="name">Kaylynn Geidt</div>
								</div>
							</li>
							<li class="person-item">
								<Avatar image="layout/images/dashboard/angel.png" v-badge="4" class="mr-2" shape="circle"></Avatar>
								<div class="person-info">
									<div class="amount">$25,338</div>
									<div class="name">Angel Rosser</div>
								</div>
							</li>
							<li class="person-item">
								<Avatar image="layout/images/dashboard/cristofer.png" v-badge="5" class="mr-2" shape="circle"></Avatar>
								<div class="person-info">
									<div class="amount">$15,989</div>
									<div class="name">Cristofer Mango</div>
								</div>
							</li>
						</ul>
					</div>
				</div>
			</div>

			<div class="col-12 lg:col-8">
				<div class="card widget-customer-graph">
					<div class="header">
						<div class="title">
							<span>Weekly new customers</span>
							<Dropdown :options="customerYear" v-model="selectedCustomerYear" optionLabel="name" @change="changeCustomerChart($event)"></Dropdown>
						</div>
						<p class="subtitle">Number of new customer are listed by weekly</p>
					</div>

					<div class="content grid grid-nogutter">
						<div class="col-12 md:col-6 grid">
							<div class="col-12 md:col-4 flex align-items-center">
								<h2>{{customerMax}}</h2>
								<p>MAX</p>
							</div>
							<div class="col-12 md:col-4 flex align-items-center">
								<h2>{{customerMin}}</h2>
								<p>MIN</p>
							</div>
							<div class="col-12 md:col-4 flex align-items-center">
								<h2 style="color:#FC6161">{{customerAvg}}</h2>
								<p>AVERAGE</p>
							</div>
						</div>
					</div>

					<Chart ref="customer" type="bar" id="customer-chart" :data="customerChart" :options="customerChartOptions"></Chart>
				</div>
			</div>

			<div class="col-12 lg:col-4">
				<div class="card widget-target">
					<div class="card-header">
						<span>Weekly target</span>
					</div>
					<div class="content">
						<h3>1232 Users</h3>
						<span class="rate">%3.5 <i class="pi pi-arrow-up"></i><span>  than last week</span></span>
					</div>
					<div class="values">
						<div class="item">
							<span>51%</span>
							<ProgressBar :value="51" :showValue="false"></ProgressBar>
							<span class="day">Thu</span>
						</div>
						<div class="item">
							<span>68%</span>
							<ProgressBar :value="68" :showValue="false"></ProgressBar>
							<span class="day">Fri</span>
						</div>
						<div class="item">
							<span>74%</span>
							<ProgressBar :value="74" :showValue="false"></ProgressBar>
							<span class="day">Sat</span>
						</div>
						<div class="item">
							<span>61%</span>
							<ProgressBar :value="61" :showValue="false"></ProgressBar>
							<span class="day">Sun</span>
						</div>
						<div class="item success">
							<span>100%</span>
							<ProgressBar :value="100" :showValue="false"></ProgressBar>
							<span class="day">Mon</span>
						</div>
						<div class="item">
							<span>70%</span>
							<ProgressBar :value="70" :showValue="false"></ProgressBar>
							<span class="day">Tue</span>
						</div>
						<div class="item today">
							<span>22%</span>
							<ProgressBar :value="22" :showValue="false"></ProgressBar>
							<span class="day">Today</span>
						</div>
					</div>
				</div>
			</div>

			<div class="col-12 widget-customer-carousel">
				<h6>Top customers</h6>
				<Carousel :value="customerCarousel" :numVisible="4" :numScroll="1" :circular="true" :responsiveOptions="carouselResponsiveOptions">
					<template #item="slotProps">
						<div class="card mr-4">
							<div class="customer-item-content">
								<div class="mb-6">
									<img :src="'layout/images/dashboard/' + slotProps.data.image + '.png'" :alt="slotProps.data.image" class="product-image" />
								</div>
								<div>
									<h4>{{slotProps.data.user}}</h4>
									<h5 class="mt-0 mb-3">{{slotProps.data.value}}</h5>
								</div>
							</div>
						</div>
					</template>
				</Carousel>
			</div>
		</div>
	</div>
</template>

<script>
import CustomerService from '../service/CustomerService';
export default {
	data() {
		return {
			customersTable: null,
			customersTable1: null,
			customersTable2: null,
			selectedVisitorYear: null,
			selectedRevenueMonth: null,
			selectedOrderYear: null,
			selectedCustomers1: null,
			selectedCustomerYear: null,
			carouselResponsiveOptions: [
				{
					breakpoint: '1024px',
					numVisible: 3,
					numScroll: 3
				},
				{
					breakpoint: '768px',
					numVisible: 2,
					numScroll: 2
				},
				{
					breakpoint: '560px',
					numVisible: 1,
					numScroll: 1
				}
			],
			visitorChart: {
				labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
				datasets: [
					{
						label: 'Plan',
						data: [630, 630, 695, 695, 695, 760, 760, 760, 840, 840, 840, 840],
						borderColor: [
							'#FC6161',
						],
						pointBorderColor: 'transparent',
						pointBackgroundColor: 'transparent',
						type: 'line',
						fill: false,
						barPercentage: 0.5,
						stepped: true
					},
					{
						label: 'Growth actual',
						data: [600, 671, 660, 665, 700, 610, 810, 790, 710, 860, 810, 780],
						backgroundColor: getComputedStyle(document.body).getPropertyValue('--primary-color') ,
						fill: true,
						barPercentage: 0.5
					}
				]
			},
			visitorChartOptions: {
				plugins: {
					legend: {
						position: 'top',
						align: 'end'
					}
				},
				responsive: true,
				hover: {
					mode: 'index'
				},
				scales: {
					y: {
						min: 500,
						max: 900,
						grid: {
							display: false
						}
					},
					x: {
						grid: {
							display: false
						}
					}
				}
			},
			growth:'$620,076',
			avgCustomer: '$1,120',
			timelineEvents: [
				{transaction: 'Payment from #28492', amount: '+$250.00', date: 'June 13, 2020 11:09 AM',
					icon: 'pi pi-check', iconColor: '#0F8BFD', amountColor: '#00D0DE'},
				{transaction: 'Process refund to #94830', amount: '-$570.00', date: 'June 13, 2020 08:22 AM',
					icon: 'pi pi-refresh', iconColor: '#FC6161', amountColor: '#FC6161'},
				{transaction: 'New 8 user to #5849', amount: '+$50.00', date: 'June 12, 2020 02:56 PM',
					icon: 'pi pi-plus', iconColor: '#0BD18A', amountColor: '#0BD18A'},
				{transaction: 'Payment from #3382', amount: '+$3830.00', date: 'June 11, 2020 06:11 AM',
					icon: 'pi pi-check', iconColor: '#0F8BFD', amountColor: '#00D0DE'},
				{transaction: 'Payment from #4738', amount: '+$845.00', date: 'June 11, 2020 03:50 AM',
					icon: 'pi pi-check', iconColor: '#0F8BFD', amountColor: '#00D0DE'},
				{transaction: 'Payment failed form #60958', amount: '$1450.00', date: 'June 10, 2020 07:54 PM',
					icon: 'pi pi-exclamation-triangle', iconColor: '#EC4DBC', amountColor: '#EC4DBC'},
				{transaction: 'Payment from #5748', amount: '+$50.00', date: 'June 09, 2020 11:37 PM',
					icon: 'pi pi-check', iconColor: '#0F8BFD', amountColor: '#00D0DE'},
				{transaction: 'Removed 32 users from #5849', amount: '-$240.00', date: 'June 09, 2020 08:40 PM',
					icon: 'pi pi-minus', iconColor: '#FC6161', amountColor: '#FC6161'},
			],
			countryChart: {
				labels: ['RUS', 'Other', 'IND', 'AUS', 'JPN', 'USA', 'CHN'],
				datasets: [
					{
						data: [30, 18, 36, 54, 61, 90, 72],
						backgroundColor: [
							'#0F8BFD',
							'#545C6B',
							'#EC4DBC',
							'#EEE500',
							'#FC6161',
							'#00D0DE',
							'#873EFE',
						],
						hoverBackgroundColor: [
							'#0F8BFD',
							'#545C6B',
							'#EC4DBC',
							'#EEE500',
							'#FC6161',
							'#00D0DE',
							'#873EFE',
						],
						borderColor: 'transparent',
						fill: true
					}
				]
			},
			countryChartOptions: {
				responsive: true
			},
			revenueChart: {
				labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
				datasets: [
					{
						label: 'Sales',
						data: [37, 34, 21, 27, 10, 18, 15],
						borderColor: '#EEE500',
						pointBackgroundColor: '#EEE500',
						backgroundColor: 'rgba(238, 229, 0, 0.05)',
						fill: true,
						tension: 0.4
					},
					{
						label: 'Revenue',
						data: [31, 27, 30, 37, 23, 29, 20],
						borderColor: '#00D0DE',
						pointBackgroundColor: '#00D0DE',
						backgroundColor: 'rgba(0, 208, 222, 0.05)',
						fill: true,
						tension: 0.4
					},
					{
						label: 'Expenses',
						data: [21, 7, 13, 3, 19, 11, 6],
						borderColor: '#FC6161',
						pointBackgroundColor: '#FC6161',
						backgroundColor: 'rgba(253, 72, 74, 0.05)',
						fill: true,
						tension: 0.4
					},
					{
						label: 'Customer',
						data: [47, 31, 35, 20, 46, 39, 25],
						borderColor: '#0F8BFD',
						pointBackgroundColor: '#0F8BFD',
						backgroundColor: 'rgba(15, 139, 253, 0.05)',
						fill: true,
						tension: 0.4
				}]
			},
			revenueChartOptions: {
				responsive: true,
				hover: {
					mode: 'index'
				},
				scales: {
					y: {
						min: 0,
						max: 50,
						ticks: {
							stepSize: 5
						}
					}
				}
			},
			customerChart: {
				labels: ['January', 'March', 'May', 'Agust', 'October', 'December'],
				datasets: [
					{
						data: [10, 25, 48, 35, 54, 70],
						backgroundColor: '#AAABDD',
						hoverBackgroundColor: '#AAABDD',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [18, 35, 23, 30, 59, 65],
						backgroundColor: '#A0A0D9',
						hoverBackgroundColor: '#A0A0D9',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [20, 47, 46, 46, 61, 70],
						backgroundColor: '#ACADDE',
						hoverBackgroundColor: '#ACADDE',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [17, 34, 18, 48, 67, 68],
						backgroundColor: '#ABABDD',
						hoverBackgroundColor: '#ABABDD',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [9, 37, 47, 50, 60, 62],
						backgroundColor: '#A2A3D9',
						hoverBackgroundColor: '#A2A3D9',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [8, 48, 40, 52, 72, 75],
						backgroundColor: '#A3A4DA',
						hoverBackgroundColor: '#A3A4DA',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [10, 18, 50, 47, 63, 80],
						backgroundColor: '#A2A3D9',
						hoverBackgroundColor: '#A2A3D9',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [20, 36, 39, 58, 59, 85],
						backgroundColor: '#8485CD',
						hoverBackgroundColor: '#8485CD',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [30, 45, 35, 50, 54, 81],
						backgroundColor: '#7D7ECA',
						hoverBackgroundColor: '#7D7ECA',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [28, 35, 52, 56, 60, 77],
						backgroundColor: '#8384CD',
						hoverBackgroundColor: '#8384CD',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [40, 40, 38, 45, 68, 86],
						backgroundColor: '#8F90D2',
						hoverBackgroundColor: '#8F90D2',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [50, 23, 27, 34, 65, 90],
						backgroundColor: '#8C8DD0',
						hoverBackgroundColor: '#8C8DD0',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [29, 27, 29, 42, 55, 84],
						backgroundColor: '#9495D4',
						hoverBackgroundColor: '#9495D4',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [10, 37, 47, 29, 59, 80],
						backgroundColor: '#9696D4',
						hoverBackgroundColor: '#9696D4',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [10, 54, 42, 38, 63, 83],
						backgroundColor: '#7273C6',
						hoverBackgroundColor: '#7273C6',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [25, 44, 50, 56, 65, 92],
						backgroundColor: '#5F60BE',
						hoverBackgroundColor: '#5F60BE',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [30, 43, 48, 45, 73, 78],
						backgroundColor: '#5C5DBD',
						hoverBackgroundColor: '#5C5DBD',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					},
					{
						data: [29, 47, 54, 60, 77, 86],
						backgroundColor: '#5C5DBD',
						hoverBackgroundColor: '#5C5DBD',
						fill: true,
						categoryPercentage: 1.0,
						barPercentage: 1.0
					}
				]
			},
			customerChartOptions: {
				interaction: {
					mode: 'x'
				},
				plugins: {
					legend: {
						display: false
					}
				},
				scales: {
					y: {
						display: false,
					},
					x: {
						grid: {
							display : false
						}
					}
				}
			},
			customerMax: '1232',
			customerMin: '284',
			customerAvg: '875',
			customerCarousel: null,
			orderYear: [
				{name: '2021', code: '0'},
				{name: '2020', code: '1'}
			],
			visitorYear: [
				{name: '2020', code: '0'},
				{name: '2019', code: '1'}
			],
			customerYear: [
				{name: '2020', code: '0'},
				{name: '2019', code: '1'}
			],
			revenueMonth: [
				{name: 'January - July 2021', code: '0'},
				{name: 'August - December 2020', code: '1'}
			]
		}
	},
	customerService: null,
	created() {
		this.customerService = new CustomerService();
	},
	mounted() {
		this.customerService.getCustomersLarge().then(customers => {
            this.customersTable = customers;
            this.customersTable.forEach(customer => customer.date = new Date(customer.date));
        });
        this.customerService.getCustomersLarge().then(customers => {
            this.customersTable1 = customers;
            this.customersTable1.forEach(customer => customer.date = new Date(customer.date));
        });
        this.customerService.getCustomersMixed().then(customers => {
            this.customersTable2 = customers;
            this.customersTable2.forEach(customer => customer.date = new Date(customer.date));
        });

		this.selectedVisitorYear = this.visitorYear[0];
		this.selectedOrderYear = this.orderYear[0];
		this.selectedCustomerYear = this.customerYear[0];
		this.selectedRevenueMonth = this.revenueMonth[0];

		this.customerCarousel = [
			{user: '9,673 Users', value: '$8,362,478', image: 'nasa'},
			{user: '9,395 Users', value: '$7,927,105', image: 'beats'},
			{user: '7,813 Users', value: '$6,471,594', image: 'gopro'},
			{user: '7,613 Users', value: '$5,697,883', image: 'north'},
			{user: '98,673 Users', value: '$7,653,311', image: 'mc'},
			{user: '5,645 Users', value: '$4,567,823', image: 'dell'},
			{user: '5,153 Users', value: '$5,342,678', image: 'wwf'},
			{user: '4,338 Users', value: '$5,867,391', image: 'bmw'},
			{user: '4,170 Users', value: '$4,647,233', image: 'pepsi'},
			{user: '3,765 Users', value: '$4,123,876', image: 'netflix'},
			{user: '3,490 Users', value: '$3,688,362', image: 'deloitte'},
			{user: '2,976 Users', value: '$3,978,478', image: 'pg'},
		];
	},
	methods: {
		changeRevenueChart(event) {
			const dataSet1 = [
				[37, 34, 21, 27, 10, 18, 15],
				[31, 27, 30, 37, 23, 29, 20],
				[21, 7, 13, 3, 19, 11, 6],
				[47, 31, 35, 20, 46, 39, 25]
			];
			const dataSet2 = [
				[31, 27, 30, 37, 23, 29, 20],
				[47, 31, 35, 20, 46, 39, 25],
				[37, 34, 21, 27, 10, 18, 15],
				[21, 7, 13, 3, 19, 11, 6]
			];

			if (event.value.code === '1') {
				this.revenueChart.datasets[0].data = dataSet2[parseInt('0')];
				this.revenueChart.datasets[1].data = dataSet2[parseInt('1')];
				this.revenueChart.datasets[2].data = dataSet2[parseInt('2')];
				this.revenueChart.datasets[3].data = dataSet2[parseInt('3')];
			} else {
				this.revenueChart.datasets[0].data = dataSet1[parseInt('0')];
				this.revenueChart.datasets[1].data = dataSet1[parseInt('1')];
				this.revenueChart.datasets[2].data = dataSet1[parseInt('2')];
				this.revenueChart.datasets[3].data = dataSet1[parseInt('3')];
			}

			this.$refs.revenue.refresh();
		},
		changeVisitorChart(event) {
			const dataSet1 = [
				[630, 630, 695, 695, 695, 760, 760, 760, 840, 840, 840, 840],
				[600, 671, 660, 665, 700, 610, 810, 790, 710, 860, 810, 780]
			];
			const dataSet2 = [
				[580, 580, 620, 620, 620, 680, 680, 680, 730, 730, 730, 730],
				[550, 592, 600, 605, 630, 649, 660, 690, 710, 720, 730, 780],
			];

			if (event.value.code === '1') {
				this.growth = '$581,259';
				this.avgCustomer = '$973';
				this.visitorChart.datasets[0].data = dataSet2[parseInt('0')];
				this.visitorChart.datasets[1].data = dataSet2[parseInt('1')];
			} else {
				this.growth = '$620,076';
				this.avgCustomer = '$1,120';
				this.visitorChart.datasets[0].data = dataSet1[parseInt('0')];
				this.visitorChart.datasets[1].data = dataSet1[parseInt('1')];
			}

			this.$refs.visitor.refresh();
		},
		changeCustomerChart(event) {
			const dataSet1 = [
				[10, 25, 48, 35, 54, 70],
				[18, 35, 23, 30, 59, 65],
				[20, 47, 46, 46, 61, 70],
				[17, 34, 18, 48, 67, 68],
				[9, 37, 47, 50, 60, 62],
				[8, 48, 40, 52, 72, 75],
				[10, 18, 50, 47, 63, 80],
				[20, 36, 39, 58, 59, 85],
				[30, 45, 35, 50, 54, 81],
				[28, 35, 52, 56, 60, 77],
				[40, 40, 38, 45, 68, 86],
				[50, 23, 27, 34, 65, 90],
				[29, 27, 29, 42, 55, 84],
				[10, 37, 47, 29, 59, 80],
				[10, 54, 42, 38, 63, 83],
				[25, 44, 50, 56, 65, 92],
				[30, 43, 48, 45, 73, 78],
				[29, 47, 54, 60, 77, 86]
			];
			const dataSet2 = [
				[10, 25, 48, 35, 54, 70],
				[20, 47, 46, 46, 61, 70],
				[17, 34, 18, 48, 67, 68],
				[50, 23, 27, 34, 65, 90],
				[8, 48, 40, 52, 72, 75],
				[9, 37, 47, 50, 60, 62],
				[10, 18, 50, 47, 63, 80],
				[30, 45, 35, 50, 54, 81],
				[10, 37, 47, 29, 59, 80],
				[28, 35, 52, 56, 60, 77],
				[25, 44, 50, 56, 65, 92],
				[18, 35, 23, 30, 59, 65],
				[20, 36, 39, 58, 59, 85],
				[29, 27, 29, 42, 55, 84],
				[40, 40, 38, 45, 68, 86],
				[30, 43, 48, 45, 73, 78],
				[10, 54, 42, 38, 63, 83],
				[29, 47, 54, 60, 77, 86]
			];

			if (event.value.code === '1') {
				this.customerAvg = '621';
				this.customerMin = '198';
				this.customerMax = '957';
				this.customerChart.datasets[0].data = dataSet2[parseInt('0')];
				this.customerChart.datasets[1].data = dataSet2[parseInt('1')];
				this.customerChart.datasets[2].data = dataSet2[parseInt('2')];
				this.customerChart.datasets[3].data = dataSet2[parseInt('3')];
				this.customerChart.datasets[4].data = dataSet2[parseInt('4')];
				this.customerChart.datasets[5].data = dataSet2[parseInt('5')];
				this.customerChart.datasets[6].data = dataSet2[parseInt('6')];
				this.customerChart.datasets[7].data = dataSet2[parseInt('7')];
				this.customerChart.datasets[8].data = dataSet2[parseInt('8')];
				this.customerChart.datasets[9].data = dataSet2[parseInt('9')];
				this.customerChart.datasets[10].data = dataSet2[parseInt('10')];
				this.customerChart.datasets[11].data = dataSet2[parseInt('11')];
				this.customerChart.datasets[12].data = dataSet2[parseInt('12')];
				this.customerChart.datasets[13].data = dataSet2[parseInt('13')];
				this.customerChart.datasets[14].data = dataSet2[parseInt('14')];
				this.customerChart.datasets[15].data = dataSet2[parseInt('15')];
				this.customerChart.datasets[16].data = dataSet2[parseInt('16')];
				this.customerChart.datasets[17].data = dataSet2[parseInt('17')];
			} else {
				this.customerAvg = '875';
				this.customerMin = '284';
				this.customerMax = '1232';
				this.customerChart.datasets[0].data = dataSet1[parseInt('0')];
				this.customerChart.datasets[1].data = dataSet1[parseInt('1')];
				this.customerChart.datasets[2].data = dataSet1[parseInt('2')];
				this.customerChart.datasets[3].data = dataSet1[parseInt('3')];
				this.customerChart.datasets[4].data = dataSet1[parseInt('4')];
				this.customerChart.datasets[5].data = dataSet1[parseInt('5')];
				this.customerChart.datasets[6].data = dataSet1[parseInt('6')];
				this.customerChart.datasets[7].data = dataSet1[parseInt('7')];
				this.customerChart.datasets[8].data = dataSet1[parseInt('8')];
				this.customerChart.datasets[9].data = dataSet1[parseInt('9')];
				this.customerChart.datasets[10].data = dataSet1[parseInt('10')];
				this.customerChart.datasets[11].data = dataSet1[parseInt('11')];
				this.customerChart.datasets[12].data = dataSet1[parseInt('12')];
				this.customerChart.datasets[13].data = dataSet1[parseInt('13')];
				this.customerChart.datasets[14].data = dataSet1[parseInt('14')];
				this.customerChart.datasets[15].data = dataSet1[parseInt('15')];
				this.customerChart.datasets[16].data = dataSet1[parseInt('16')];
				this.customerChart.datasets[17].data = dataSet1[parseInt('17')];
			}
			
			this.$refs.customer.refresh();
		},
		recentSales(event) {
			if (event.value.code === '0') {
				this.customersTable = this.customersTable1;
			} else {
				this.customersTable = this.customersTable2;
			}
		},
		formatDate(value) {
            return value.toLocaleDateString('en-US', {
                day: '2-digit',
                month: '2-digit',
                year: 'numeric',
            });
        },
		formatCurrency(value) {
            return value.toLocaleString('en-US', {style: 'currency', currency: 'USD'});
        }
	}
}
</script>

<style lang="scss" scoped>
::v-deep(.p-progressbar) {
	height: .5rem;
	background-color: #D8DADC;

	.p-progressbar-value {
		background-color: #607D8B;
	}
}
</style>