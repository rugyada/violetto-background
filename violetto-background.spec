# Violetto theme background
%define oname Violetto
%define bdate   2022.02.14

Summary:	Violetto theme background
Name:		violetto-background
Version:	1.0
Release:	3
License:	GPL
Group:		Graphics
Url:		https://github.com/rugyada/violetto-background
Source0:	%{oname}.tar.gz

BuildArch:	noarch

%description
Violetto theme background

%files
%{_datadir}/wallpapers/Violetto

%prep

%build

%install
# mkdir -p %{buildroot}%{_datadir}/wallpapers/Violetto
install -d -m 0755 %{buildroot}/%{_datadir}/wallpapers/Violetto/Violetto-*.png
