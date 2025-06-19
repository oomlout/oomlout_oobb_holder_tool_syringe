$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-5.7500000000, 5.7500000000, 0]) {
				cylinder(h = 15, r = 5);
			}
			translate(v = [5.7500000000, 5.7500000000, 0]) {
				cylinder(h = 15, r = 5);
			}
			translate(v = [-5.7500000000, -5.7500000000, 0]) {
				cylinder(h = 15, r = 5);
			}
			translate(v = [5.7500000000, -5.7500000000, 0]) {
				cylinder(h = 15, r = 5);
			}
		}
	}
	union() {
		#translate(v = [0, 0, 3.0000000000]) {
			cylinder(h = 12, r1 = 2.7500000000, r2 = 3.2500000000);
		}
	}
}