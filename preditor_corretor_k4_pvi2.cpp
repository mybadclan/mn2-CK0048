#include <iostream>
//#include <bits/stdc++.h>
#include <cmath>

#include "runge_kutta_k4_pvi2.cpp"

using namespace std;

struct Estado {
  double v, y;
};

double v_i_menos_k(double &v, double &m, double &k, double &t, double &g){
  return -g - (k/m) * v;
}

double predicao_v(double &v, double &m, double &k, double &t, double &g, double &v3, double &v2, double &v1){
  return v + t/24.0 * (55.0* (-g - (k/m) * v) - 59.0 * (-g - (k/m) * v3/*v_i_menos_k(v3, m, k, t, g)*/)
    + 37.0*(-g - (k/m) *v2/*v_i_menos_k(v2, m, k, t, g)*/)
    - 9.0*(-g - (k/m) *v1/*v_i_menos_k(v1, m, k, t, g)*/));
}

double predicao_y(double &y, double &v, double &m, double &k, double &t, double &g, double &v3, double &v2, double &v1){
  return y + t/24.0 * (55.0*v - 59.0*v3 + 37.0*v2 - 9.0*v1);
}

double correcao_v(double &v, double &m, double &k, double &t, double &g, double &v2, double &v3, double &vi_mais_1){
  return v + t/24.0 * (-40.0* (-g - (k/m) * v2) + 118.0 * (-g - (k/m) * v3)
    - 104.0*(-g - (k/m) *v)
    + 50.0*(-g - (k/m) *vi_mais_1));
}

double correcao_y(double &y, double &v, double &m, double &k, double &t, double &g, double &v2, double &v3, double &vi_mais_1){
  return y + t/24.0 * (-40.0*v2 + 118.0*v3 - 104.0*v + 50.0*vi_mais_1);
}

int main(){
  double y = 200.0, v = 5.0, m = 2.0, k = 0.25, t = 0.1, g = 10.0, t_seq=0.1;

  double vel_exata;

  double vel = v;

  double y_exata, y_max=y, t_subida=0.0;

  double y_i = y;

  double erro_vel;

  double erro_y;

  Estado s1, s2, s3, s_barra_i_mais_1, s_i_mais_1, s_temp;

  for (int j =0;j<4;++j){
    for (int i =1;i<4;++i){
      y_i = y_queda_livre(y_i, vel, m, k, t, g);
    
      vel = v_queda_livre(vel, m, k, t, g);
      if (i==1){
        s1.y = y_i;
        s1.v = vel;
      }
      if (i==2){
        s2.y = y_i;
        s2.v = vel;
      }
      if (i==3){
        s3.y = y_i;
        s3.v = vel;
      }
      if (vel > 0){
        y_max = y_i;
        t_subida = t*i;
      }
    }
    int passos = 3;
    //y_i = y_queda_livre(y_i, vel, m, k, t, g);
    
    //vel = v_queda_livre(vel, m, k, t, g);
    
    //s_temp.v = vel;
    //s_temp.y = y_i;
    //s_i_mais_1.v = vel;
    s_i_mais_1.y = y_i;
    
    while (s_i_mais_1.y > 0){
      ++passos;
      s_barra_i_mais_1.y = predicao_y(s3.y, s3.v, m, k, t, g, s3.v, s2.v, s1.v);
      s_barra_i_mais_1.v = predicao_v(s3.v, m, k, t, g, s3.v, s2.v, s1.v);
      do {
        s_i_mais_1.y = correcao_y(s3.y, s3.v, m, k, t, g, s2.v, s3.v, s_barra_i_mais_1.v);
        s_i_mais_1.v = correcao_v(s3.v, m, k, t, g, s2.v, s3.v, s_barra_i_mais_1.v);
      }
      while (abs( ((s_i_mais_1.v - s_barra_i_mais_1.v) / s_i_mais_1.v)) < 0.000000001  );
      //cout << abs( ((s_i_mais_1.v - s_barra_i_mais_1.v) / s_i_mais_1.v)) << '\n';
      if (s_i_mais_1.v > 0){
        y_max = y_i;
        t_subida = t*passos;
      }
      s1.v = s2.v;
      s1.y = s2.y;
      s2.v = s3.v;
      s2.y = s3.y;
      s3.v = s_i_mais_1.v;
      s3.y = s_i_mais_1.y;
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
    cout << s_i_mais_1.y << "\t\t| " << t << '\n';
    cout << "erro relativo y:\t" << erro_y << '\n';
    cout << "erro relativo vel:\t" << erro_vel << '\n';
    cout << "velocidade:\t" << s_i_mais_1.v << '\n';
    cout << "------------------------------------------\n";
    t = t_seq/10.0;
    t_seq = t;
    y_i = 200.0;
    vel = 5.0;
    t_subida = 0.0;
    y_max = y_i;
    s_i_mais_1.y = 1.0;
  }
}