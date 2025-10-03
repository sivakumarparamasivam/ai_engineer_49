from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from typing import Optional, List, Union


class DataVisualization:
    """Comprehensive data visualization suite"""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self._setup_style()
    
    def _setup_style(self):
        """Setup matplotlib style"""
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        plt.rcParams['figure.figsize'] = (12, 6)
        plt.rcParams['font.size'] = 10
    
    def plot_distribution(self, column: str, plot_type: str = 'hist',
                         bins: int = 30, kde: bool = True,
                         save_path: Optional[str] = None) -> plt.Figure:
        """
        Plot distribution of a column
        
        Args:
            column: Column name
            plot_type: 'hist', 'box', 'violin', 'kde'
            bins: Number of bins for histogram
            kde: Show KDE overlay for histogram
            save_path: Path to save figure
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if plot_type == 'hist':
            self.data[column].hist(bins=bins, ax=ax, alpha=0.7, edgecolor='black')
            if kde:
                self.data[column].plot(kind='kde', ax=ax, secondary_y=True, color='red', linewidth=2)
            ax.set_ylabel('Frequency')
        
        elif plot_type == 'box':
            self.data.boxplot(column=column, ax=ax)
            ax.set_ylabel('Value')
        
        elif plot_type == 'violin':
            sns.violinplot(data=self.data, y=column, ax=ax)
        
        elif plot_type == 'kde':
            self.data[column].plot(kind='kde', ax=ax, linewidth=2)
            ax.set_ylabel('Density')
        
        ax.set_xlabel(column)
        ax.set_title(f'Distribution of {column}', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        return fig
    
    def plot_correlation_heatmap(self, columns: Optional[List[str]] = None,
                                method: str = 'pearson',
                                annot: bool = True,
                                save_path: Optional[str] = None) -> plt.Figure:
        """Plot correlation heatmap"""
        cols = columns if columns else self.data.select_dtypes(include=[np.number]).columns
        corr = self.data[cols].corr(method=method)
        
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(corr, annot=annot, cmap='coolwarm', center=0,
                   square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                   fmt='.2f', ax=ax)
        ax.set_title(f'Correlation Heatmap ({method.capitalize()})', 
                    fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        return fig
    
    def plot_scatter(self, x: str, y: str, hue: Optional[str] = None,
                    size: Optional[str] = None, alpha: float = 0.6,
                    save_path: Optional[str] = None) -> plt.Figure:
        """Plot scatter plot with optional hue and size"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if hue:
            for category in self.data[hue].unique():
                mask = self.data[hue] == category
                ax.scatter(self.data.loc[mask, x], self.data.loc[mask, y],
                          label=category, alpha=alpha, s=100)
            ax.legend(title=hue)
        else:
            ax.scatter(self.data[x], self.data[y], alpha=alpha, s=100)
        
        ax.set_xlabel(x, fontsize=12)
        ax.set_ylabel(y, fontsize=12)
        ax.set_title(f'{y} vs {x}', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        return fig
    
    def plot_bar_chart(self, x: str, y: str, 
                      horizontal: bool = False,
                      top_n: Optional[int] = None,
                      save_path: Optional[str] = None) -> plt.Figure:
        """Plot bar chart"""
        data = self.data.copy()
        
        if top_n:
            data = data.nlargest(top_n, y)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if horizontal:
            ax.barh(data[x], data[y], alpha=0.7)
            ax.set_xlabel(y, fontsize=12)
            ax.set_ylabel(x, fontsize=12)
        else:
            ax.bar(data[x], data[y], alpha=0.7)
            ax.set_xlabel(x, fontsize=12)
            ax.set_ylabel(y, fontsize=12)
            plt.xticks(rotation=45, ha='right')
        
        ax.set_title(f'{y} by {x}', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y' if not horizontal else 'x')
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        return fig
    
    def plot_line_chart(self, x: str, y: Union[str, List[str]],
                       hue: Optional[str] = None,
                       markers: bool = True,
                       save_path: Optional[str] = None) -> plt.Figure:
        """Plot line chart"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        y_cols = [y] if isinstance(y, str) else y
        
        if hue:
            for category in self.data[hue].unique():
                mask = self.data[hue] == category
                for y_col in y_cols:
                    ax.plot(self.data.loc[mask, x], self.data.loc[mask, y_col],
                           marker='o' if markers else None, 
                           label=f'{category} - {y_col}')
        else:
            for y_col in y_cols:
                ax.plot(self.data[x], self.data[y_col],
                       marker='o' if markers else None, label=y_col)
        
        ax.set_xlabel(x, fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.set_title('Time Series Plot', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        return fig
    
    def plot_multiple_distributions(self, columns: List[str],
                                   save_path: Optional[str] = None) -> plt.Figure:
        """Plot multiple distributions in subplots"""
        n_cols = len(columns)
        n_rows = (n_cols + 2) // 3
        
        fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5*n_rows))
        axes = axes.flatten() if n_rows > 1 else [axes]
        
        for idx, col in enumerate(columns):
            if pd.api.types.is_numeric_dtype(self.data[col]):
                self.data[col].hist(bins=30, ax=axes[idx], alpha=0.7, edgecolor='black')
                axes[idx].set_title(col, fontweight='bold')
                axes[idx].set_ylabel('Frequency')
                axes[idx].grid(True, alpha=0.3)
        
        # Hide unused subplots
        for idx in range(len(columns), len(axes)):
            axes[idx].set_visible(False)
        
        plt.suptitle('Distribution Analysis', fontsize=16, fontweight='bold', y=1.00)
        plt.tight_layout()
        
        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        return fig
