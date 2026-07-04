from flask import Flask, render_template, request, jsonify, session
import math

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  
class SolarCalculator:
    @staticmethod
    def compute_detailed_system(config_data, devices):
        try:
            total_wh = 0
            t_watt = 0
            
            # Process device data
            for device in devices:
                watts = float(device['watts'])
                hours = float(device['hours'])
                total_wh += watts * hours
                t_watt += watts

            system_loss_factor = 1.3
            panel_gen_factor = 3.43
            
            voltage = float(config_data['voltage'])
            panel_rating = float(config_data['panel_rating'])
            isc = float(config_data['isc'])
            days_autonomy = float(config_data['days_autonomy'])
            derating_factor = float(config_data['derating_factor'])
            depth_of_discharge = float(config_data['depth_of_discharge'])

            required_wh = total_wh * system_loss_factor
            total_wp = required_wh / panel_gen_factor
            num_panels = math.ceil(total_wp / panel_rating)

            inverter_size = t_watt * 1.25
            battery_ah = (total_wh * days_autonomy) / (derating_factor * depth_of_discharge * voltage)
            
            charge_ctrl_rating = math.ceil(num_panels * isc * 1.3)

            result = {
                "total_wh": f"{total_wh:.2f}",
                "required_wh": f"{required_wh:.2f}",
                "total_wp": f"{total_wp:.2f}",
                "num_panels": int(num_panels),
                "panel_rating": int(panel_rating),
                "inverter_size": f"{inverter_size:.2f} or greater",
                "battery_ah": f"{battery_ah:.2f}",
                "voltage": voltage,
                "charge_ctrl_rating":   charge_ctrl_rating + 1,
                "system_loss_factor": system_loss_factor,
                "panel_gen_factor": panel_gen_factor,
                "days_autonomy": days_autonomy,
                "derating_factor": derating_factor,
                "depth_of_discharge": depth_of_discharge
            }

            session['solar_results'] = {
                "battery_ah": f"{battery_ah:.2f}",
                "voltage": voltage,
                "num_panels": int(num_panels),
                "panel_rating": int(panel_rating),
                "inverter_size": f"{inverter_size:.2f}",
                "charge_ctrl_rating": charge_ctrl_rating + 1
            }
            return result

        except Exception as e:
            return {"error": f"Invalid input: {str(e)}"}

    def compute_system_size(monthly_bill, actual_consumption):
        try:
            rate = monthly_bill / actual_consumption
            tpd = actual_consumption / 30
            size = tpd / (24 * 0.16)
            s = int(size + 1)
            
            return {
                "daily_consumption": f"{tpd:.2f}",
                "rate": f"{rate:.2f}",
                "system_size": f"{s}-{s+1}"
            }
        except Exception as e:
            return {"error": str(e)}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/system-size')
def system_size():
    return render_template('system_size.html')

@app.route('/detailed-calculator')
def detailed_calculator():
    return render_template('detailed_calc.html')

@app.route('/api/calculate-system-size', methods=['POST'])
def api_calculate_system_size():
    data = request.get_json()
    monthly_bill = float(data['monthly_bill'])
    actual_consumption = float(data['actual_consumption'])
    result = SolarCalculator.compute_system_size(monthly_bill, actual_consumption)
    return jsonify(result)

@app.route('/materials')
def materials():
    return render_template('materials.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/api/calculate-detailed-system', methods=['POST'])
def api_calculate_detailed_system():
    data = request.get_json()
    config_data =  data['config_data']
    devices = data['devices']
    result = SolarCalculator.compute_detailed_system(config_data, devices)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)