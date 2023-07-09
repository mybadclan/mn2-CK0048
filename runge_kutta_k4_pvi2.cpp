#include <iostream>
//#include <bits/stdc++.h>
#include <cmath>

using namespace std;

double v_barra_2_por_2_queda_livre(double &v, double &m, double &k, double &t, double &g){
  return v + t/2.0 * (-g - (k/m) * v);
}

double y_barra_2_por_2_queda_livre(double y, double &v, double &m, double &k, double &t, double &g){
  return y + t/2.0 * v;
}

double v_barra_3_queda_livre(double &v, double &m, double &k, double &t, double &g){
  return v + t/2.0 * (-g - (k/m) * v_barra_2_por_2_queda_livre(v, m, k, t, g));
}

double y_barra_3_queda_livre(double y, double &v, double &m, double &k, double &t, double &g){
  return y + t * v_barra_2_por_2_queda_livre(v, m, k, t, g);
}

double v_barra_4_queda_livre(double &v, double &m, double &k, double &t, double &g){
  return v + t * (-g - (k/m) * v_barra_3_queda_livre(v, m, k, t, g));
}

double y_barra_4_queda_livre(double y, double &v, double &m, double &k, double &t, double &g){
  return y + t * v_barra_3_queda_livre(v, m, k, t, g);
}

double v_queda_livre(double &v, double &m, double &k, double &t, double &g){
  return v + t *(1.0/6.0) * ( (-g - (k/m) * v) + 2.0*(-g - (k/m) * v_barra_2_por_2_queda_livre(v, m, k, t, g)) 
    + 2.0*(-g - (k/m) * v_barra_3_queda_livre(v, m, k, t, g)) 
    + (-g - (k/m) * v_barra_4_queda_livre(v, m, k, t, g)));
}

double y_queda_livre(double y, double &v, double &m, double &k, double &t, double &g){
  return y + t * (1.0/6.0) * ( v + 2.0*v_barra_2_por_2_queda_livre(v, m, k, t, g)
    + 2.0*v_barra_3_queda_livre(v, m, k, t, g)
    + v_barra_4_queda_livre(v, m, k, t, g));
}

double erro_relativo_vel(double v_exata, double v_aprox){
  return (v_exata - v_aprox) / v_exata;
}

double erro_relativo_y(double y_exata, double y_aprox){
  return (y_exata - y_aprox) / y_exata;
}

double v_solucao_exata(double &v, double &m, double &k, double &t, double &g){
  return -g*(m/k) + (v + g*(m/k)) * exp(-(k/m)*t);
}

double y_solucao_exata(double &y, double &v, double &m, double &k, double &t, double &g){
  return y-g*(m/k)*t - (v + g*(m/k)) * m/k * (exp(-(k/m)*t) - 1);
}
/*
int main(){
  double y = 200.0, v = 5.0, m = 2.0, k = 0.25, t = 0.1, g = 10.0, t_seq=0.1;

  double vel_exata;

  double vel = v_queda_livre(v, m, k, t, g);

  double y_exata, y_max, t_subida=0.0;

  double y_i = y_queda_livre(y, v, m, k, t, g);

  double erro_vel;

  double erro_y;

  for (int i =0;i<4;++i){
    int passos = 1;
    while (y_i > 0){
      if (vel > 0){
        y_max = y_i;
        t_subida = t*passos;
      }
      ++passos;
      y_i = y_queda_livre(y_i, vel, m, k, t, g);
  
      vel = v_queda_livre(vel, m, k, t, g);
  
    }
    t = t * passos;
    vel_exata = v_solucao_exata(v, m, k, t, g);

    y_exata = y_solucao_exata(y, v, m, k, t, g);
    
    erro_vel = erro_relativo_vel(vel_exata, vel);
  
    erro_y = erro_relativo_y(y_exata, y_i);

    cout << "calculo para o delta t\t" << t_seq << '\n';
    cout << "tempo subida\t| altura maxima\n";
    cout << t_subida << "\t| " << y_max << '\n';
    cout << "y aproximado\t| " << "delta t\n";
    cout << y_i << "\t\t| " << t << '\n';
    cout << "erro relativo y:\t" << erro_y << '\n';
    cout << "erro relativo vel:\t" << erro_vel << '\n';
    cout << "velocidade:\t" << vel << '\n';
    cout << "------------------------------------------\n";
    t = t_seq/10.0;
    t_seq = t;
    y_i = 200.0;
    vel = 5.0;
    t_subida = 0.0;
    //break;
  }
}
*/