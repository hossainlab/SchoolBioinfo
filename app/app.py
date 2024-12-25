import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt
import random

# Function to calculate offspring probabilities
def calculate_offspring(parent1, parent2, num_offspring=1000):
    offspring = []
    for _ in range(num_offspring):
        allele1 = random.choice(parent1)
        allele2 = random.choice(parent2)
        offspring.append(''.join(sorted(allele1 + allele2)))  # Sort for consistency
    return Counter(offspring)

# Streamlit app
def main():
    st.title("Mendelian Inheritance Predictor")
    st.write("Predict offspring genotypes based on parental genotypes.")

    # Input parental genotypes
    parent1 = st.text_input("Enter Parent 1 genotype (e.g., Aa):", "Aa")
    parent2 = st.text_input("Enter Parent 2 genotype (e.g., Aa):", "Aa")
    num_offspring = st.slider("Number of offspring to simulate:", min_value=100, max_value=10000, value=1000)

    # Validate inputs
    if len(parent1) == 2 and len(parent2) == 2:
        # Calculate probabilities
        offspring_distribution = calculate_offspring(parent1, parent2, num_offspring)

        # Display results
        st.subheader("Genotype Distribution:")
        for genotype, count in offspring_distribution.items():
            st.write(f"{genotype}: {count} ({(count / num_offspring) * 100:.2f}%)")

        # Visualization
        st.subheader("Visualization:")
        genotypes = list(offspring_distribution.keys())
        counts = list(offspring_distribution.values())

        fig, ax = plt.subplots()
        ax.bar(genotypes, counts, color=['blue', 'orange', 'green'])
        ax.set_xlabel("Genotype")
        ax.set_ylabel("Frequency")
        ax.set_title("Offspring Genotype Distribution")
        st.pyplot(fig)

    else:
        st.error("Please enter valid genotypes for both parents (e.g., Aa, AA, or aa).")

# Run the app
if __name__ == "__main__":
    main()