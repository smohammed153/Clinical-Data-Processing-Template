import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class ClinicalDataProcessor:
    """Template for processing clinical patient data"""
    
    def __init__(self):
        self.patient_data = None
        self.cleaned_data = None
    
    def generate_sample_data(self):
        """Create sample patient data for demonstration"""
        np.random.seed(42)
        
        data = {
            'patient_id': range(1, 101),
            'age': np.random.randint(18, 90, 100),
            'gender': np.random.choice(['M', 'F'], 100),
            'blood_pressure_sys': np.random.randint(100, 180, 100),
            'blood_pressure_dia': np.random.randint(60, 110, 100),
            'heart_rate': np.random.randint(50, 120, 100),
            'temperature': np.random.normal(37, 0.5, 100),
            'has_condition': np.random.choice([0, 1], 100, p=[0.7, 0.3])
        }
        
        self.patient_data = pd.DataFrame(data)
        return self.patient_data
    
    def clean_data(self):
        """Data cleaning and preprocessing steps"""
        df = self.patient_data.copy()
        
        # Handle missing values
        df = df.dropna()
        
        # Create derived features
        df['bp_category'] = pd.cut(df['blood_pressure_sys'], 
                                 bins=[0, 120, 140, 200],
                                 labels=['Normal', 'Elevated', 'High'])
        
        df['age_group'] = pd.cut(df['age'],
                               bins=[0, 30, 50, 70, 100],
                               labels=['Young', 'Middle', 'Senior', 'Elderly'])
        
        self.cleaned_data = df
        return df
    
    def generate_report(self):
        """Generate basic clinical insights"""
        if self.cleaned_data is None:
            self.clean_data()
        
        report = {
            'total_patients': len(self.cleaned_data),
            'avg_age': self.cleaned_data['age'].mean(),
            'condition_prevalence': self.cleaned_data['has_condition'].mean(),
            'bp_distribution': self.cleaned_data['bp_category'].value_counts().to_dict()
        }
        
        return report

# Example usage
processor = ClinicalDataProcessor()
sample_data = processor.generate_sample_data()
cleaned_data = processor.clean_data()
insights = processor.generate_report()

print("Clinical Insights:", insights)